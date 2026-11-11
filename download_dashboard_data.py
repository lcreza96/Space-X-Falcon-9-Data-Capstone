#!/usr/bin/env python3
"""Download the dashboard CSV from its original IBM Skills Network URL.

Usage:
    python download_dashboard_data.py
    python download_dashboard_data.py --force

The file is saved next to this script so the existing Dash app can read it.
"""

import argparse
import csv
import os
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)
DESTINATION = Path(__file__).resolve().parent / "spacex_launch_dash.csv"
REQUIRED_COLUMNS = {"Launch Site", "Payload Mass (kg)", "class"}


def download(force: bool = False) -> None:
    if DESTINATION.exists() and not force:
        print(f"Already exists: {DESTINATION}")
        print("Use --force to replace the existing file.")
        return

    temp_path = None
    try:
        request = Request(URL, headers={"User-Agent": "Falcon9-Capstone-Learning/1.0"})
        with urlopen(request, timeout=30) as response:
            with tempfile.NamedTemporaryFile(
                mode="wb", dir=DESTINATION.parent, prefix=".spacex_dash_",
                suffix=".tmp", delete=False
            ) as output:
                temp_path = Path(output.name)
                while True:
                    chunk = response.read(64 * 1024)
                    if not chunk:
                        break
                    output.write(chunk)

        if not temp_path.stat().st_size:
            raise ValueError("The downloaded dataset is empty.")

        with temp_path.open("r", newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            found = set(reader.fieldnames or [])
            missing = REQUIRED_COLUMNS - found
            if missing:
                raise ValueError(f"Unexpected CSV headers; missing: {sorted(missing)}")
            if next(reader, None) is None:
                raise ValueError("The CSV has no data rows.")

        os.replace(temp_path, DESTINATION)
        temp_path = None
        print(f"Saved dashboard dataset to: {DESTINATION}")
        print("Now run: python spacex-dash-luis-app.py")
    except (HTTPError, URLError, TimeoutError, ValueError, OSError) as error:
        raise SystemExit(
            f"Dataset download failed: {error}\n"
            "You can also download the CSV from the IBM source URL listed in "
            "DATA_SOURCES.md and place it beside the Dash app."
        ) from error
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Replace an existing local CSV")
    args = parser.parse_args()
    download(force=args.force)
