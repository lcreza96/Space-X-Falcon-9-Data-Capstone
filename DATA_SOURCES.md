# Data sources, attribution, and reuse notes

This document describes where the input data and teaching materials for the Falcon 9 landing-prediction capstone originate. **It is attribution and due-diligence documentation, not a legal opinion or a license grant.**

## 1. Data sources

### A. r/SpaceX API (community maintained)

- **Project:** https://github.com/r-spacex/SpaceX-API
- **Documentation:** https://docs.spacexdata.com/
- **Role in this project:** Structured information about launches, rockets, payloads, launchpads, and related launch properties in the API data-collection notebook.
- **Status:** The source GitHub repository was archived on June 6, 2026 and is read-only. Availability and freshness of its API endpoints can change.
- **Rights note:** The *source-code repository* specifies the Apache License 2.0. That software license should **not** automatically be assumed to grant unrestricted rights to every dataset, image, third-party record, or trademark referenced by the API.

The API is not an official SpaceX service, and this analysis makes no claim of SpaceX endorsement.

### B. Wikipedia launch records

- **Page:** https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches
- **Role in this project:** Historical launch-table information used in the web-scraping notebook.
- **Attribution:** Credit Wikipedia contributors, identify the page, and link to the original article and its page history for contributors.
- **Rights note:** Wikipedia article text is generally available under Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), with possible exceptions and separate licenses for images or other embedded material. Attribution and share-alike conditions can apply when copying/adapting protected material; individual facts may not be copyrightable. Verify the current page footer and applicable jurisdiction before republishing substantial content.
- **License link:** https://creativecommons.org/licenses/by-sa/4.0/

Any tabular information was parsed, cleaned, and reorganized for the educational analysis. Dates, launch outcomes, and similar factual data should not be confused with copying protected narrative text or third-party images.

### C. IBM Skills Network course datasets

The IBM course materials provide prepared snapshots used for specific exercises. These are **course-provided learning datasets**, not automatically open-licensed databases.

**Dash lab input (required to run the current dashboard)**

- **Filename:** `spacex_launch_dash.csv`
- **IBM source:** https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv
- **IBM lab instructions:** https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/Build_a_Dashboard_Application_with_Plotly_Dash.pdf
- **Use:** Download locally using `python download_dashboard_data.py`. The dataset is not included in this documentation package.

**SQL lab input**

- **Filename:** `Spacex.csv`
- **IBM source:** https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv
- **Use:** Dataset referenced in the repository's SQL notebook.

**Other notebook input/output files**

The notebooks may produce or require names such as `dataset_part_1.csv`, `dataset_part_2.csv`, and `spacex_launch_geo.csv`. Their exact origin and generation steps vary by notebook. Review the URLs and export statements within each notebook rather than attributing all of them to one provider.

**Rights note:** IBM / Skills Network instructional templates, text, lab questions, sample datasets, and images may have terms or rights separate from the general licenses of public sources. The fact that a file is downloadable for a lab does not, by itself, prove that bulk redistribution is permitted. This package links to the provider-hosted sources rather than bundling the CSVs.

## 2. Learner work versus course-provided material

This repository documents completed exercises in the IBM Data Science Professional Certificate's Applied Data Science Capstone. The IBM / Skills Network labs provide the educational framework, scaffolding, examples, and some source materials. Code completions, analysis steps, visualizations, interpretation, and repository organization reflect the learner's work following those labs.

A public GitHub submission is part of the course workflow, but submission instructions should not be interpreted as a universal open-source license for all teaching assets or source data.

## 3. Practical sharing policy for this project

- Share original analysis, visualizations, and code while clearly identifying IBM-provided scaffolding.
- Link to provider-hosted learning datasets where rights to redistribute a copy are not established.
- Attribute public data sources and honor any applicable copyright, database rights, usage terms, and license requirements.
- Do not include API keys, tokens, passwords, personal records, or employer-confidential information.
- Review notebook cell outputs before pushing; notebooks can embed images, downloaded data, or local environment details.
- Avoid a blanket open-source LICENSE declaration that purports to license third-party materials.

## 4. Reuse disclaimer

No original files or datasets supplied by SpaceX, IBM, Wikipedia contributors, or r/SpaceX API contributors are relicensed by this document. Any reuse beyond personal/course analysis should be evaluated using the relevant source terms.

The underlying records concern historical spaceflight events rather than patient/customer records; the current educational analysis is not intended to process GDPR-protected personal information. That does not replace checking new datasets before publication.

*Last source review: November 11, 2026.*
