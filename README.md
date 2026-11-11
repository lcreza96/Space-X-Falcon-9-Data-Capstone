# Falcon 9 First-Stage Landing Prediction

**An end-to-end data science capstone project exploring the factors associated with successful SpaceX Falcon 9 first-stage booster landings.**

This repository documents my work for the **Applied Data Science Capstone** in the **IBM Data Science Professional Certificate**. It combines Python data collection, cleaning, exploratory analysis, SQL, interactive visualizations, geographic analysis, and machine learning.

> **Scope:** The outcome analyzed here is **first-stage booster landing success**, not whether a launch reached orbit. This is an educational, historical-data analysis rather than an operational SpaceX prediction system.

## Questions explored

- How do launch site, payload mass, orbit type, and flight history relate to first-stage landing outcomes?
- How do successful landings vary across sites and missions in the course dataset?
- Can common classification models predict first-stage landing outcomes using the available features?

## Tools and methods

| Area | Main tools |
| --- | --- |
| Data collection | Python, Requests, Beautiful Soup |
| Data preparation and analysis | Pandas, NumPy, SQL / SQLite |
| Statistical visualization | Matplotlib, Seaborn |
| Interactive visualization | Plotly, Dash |
| Geographic analysis | Folium |
| Machine learning | Scikit-learn |
| Working environment | Jupyter notebooks, Python |

## Project files

| File | What it covers |
| --- | --- |
| [01 · API data collection](jupyter-labs-spacex-data-collection-api-v2_Part1.ipynb) | Request historical launch information from the community-maintained SpaceX API and prepare a structured dataset. |
| [02 · Wikipedia web scraping](jupyter-labs-webscraping%20-%20Part%202.ipynb) | Extract and structure Falcon 9 launch records from Wikipedia using Beautiful Soup. |
| [03 · Data cleaning and wrangling](labs-jupyter-spacex-Data%20wrangling_Part3.ipynb) | Prepare launch records, handle missing values, and build the landing-outcome target. |
| [04 · Exploratory analysis with SQL](jupyter-labs-eda-sql-coursera_sqllite_Part4.ipynb) | Query launch sites, payload characteristics, booster versions, and outcomes using SQL. |
| [05 · Statistical data visualization](edadataviz_ExploratoryDataAnalaysis_Part5.ipynb) | Investigate success rates and relationships between orbit, payload mass, and flight history. |
| [06 · Geospatial analysis with Folium](lab_jupyter_launch_site_location-Part6.ipynb) | Map launch locations and examine their geographic context. |
| [07 · Machine learning](SpaceX_Machine%20Learning%20Prediction_Part_7.ipynb) | Explore classification models for predicting the success of first-stage landings. |
| [`spacex-dash-luis-app.py`](spacex-dash-luis-app.py) | Interactive Dash dashboard with launch-site selection, a landing-success summary, and a payload-mass filter. |
| [`download_dashboard_data.py`](download_dashboard_data.py) | Download the course-provided CSV needed by the dashboard, without committing the data file. |
| [`DATA_SOURCES.md`](DATA_SOURCES.md) | Original sources, attribution, and reuse considerations. |
| [`requirements.txt`](requirements.txt) | Python packages needed for the project. |

## Run the Dash dashboard locally

**Prerequisites:** Python 3.10 or later and an internet connection to retrieve the IBM course dataset. Run the following commands from the repository's root directory.

1. Clone the repository:

   ```bash
   git clone https://github.com/lcreza96/Space-X-Falcon-9-Data-Capstone.git
   cd Space-X-Falcon-9-Data-Capstone
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Download the IBM dashboard dataset into the root folder:

   ```bash
   python download_dashboard_data.py
   ```

   This produces the file `spacex_launch_dash.csv`, which is used by the existing app. If you obtained the CSV through the IBM course directly, you can put it in the same folder instead.

5. Start the application:

   ```bash
   python spacex-dash-luis-app.py
   ```

6. Open **http://127.0.0.1:8050/** in a browser. Stop the local server using `Ctrl+C`.

**Note:** These instructions describe the application's dependencies and input file; they are not a claim that the dashboard has been independently tested across all Python/package versions.

## Explore the notebooks

The notebooks follow the IBM lab sequence from data collection to prediction. To browse them locally:

```bash
jupyter lab
```

Some notebooks use course-specific file paths, internet-hosted datasets, SQL notebook magic commands, or environments supplied in IBM Skills Network. Running them from top to bottom outside the course may require downloading the files referenced inside each notebook and adapting paths or SQL connections. See [`DATA_SOURCES.md`](DATA_SOURCES.md).

## Origin and attribution

This project was completed as **learner coursework** based on lab notebooks and instructions supplied by **IBM / Skills Network** as part of the IBM Data Science Professional Certificate. The original teaching materials, prompts, and any included instructional imagery belong to their respective rights holders. The completed analysis, code edits, and observations in these files reflect my work following the labs.

Source data includes:

- [Community-maintained r/SpaceX API](https://github.com/r-spacex/SpaceX-API) (not an official SpaceX API).
- [Wikipedia: List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches).
- [IBM Skills Network course-provided datasets](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv) for specific labs.

See **[DATA_SOURCES.md](DATA_SOURCES.md)** for details and reuse considerations. This project is not affiliated with, endorsed by, or sponsored by SpaceX.

## Licensing and privacy

The repository intentionally does **not** apply a blanket license to third-party notebooks, instructional content, or datasets. The r/SpaceX API **software repository** uses Apache-2.0, but that alone does not establish the license for all data exposed through the API. Wikipedia's reusable written content generally carries **CC BY-SA 4.0** requirements; reusers should verify the relevant page and the kind of material reused. IBM course assets may have separate rights or terms.

The analysis uses historical spaceflight records and is **not intended to contain identifiable customer or patient data**. Publicly accessible data should nevertheless be checked for licensing and privacy restrictions before being republished.

---

**Repository:** [lcreza96 / Space-X-Falcon-9-Data-Capstone](https://github.com/lcreza96/Space-X-Falcon-9-Data-Capstone)  
**Project type:** Data science learning portfolio / IBM capstone
