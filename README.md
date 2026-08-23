# Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics — Group 2

**Turning public health data into actionable decision analytics for outbreak
monitoring, resource planning and programme coverage.**

Dashboard 5 — *Health Programs & Population Vulnerability*

Built by **Samuel Manoj Pinipe** (Group 2) as part of the project internship,
July – August 2026.

---

## About this repository

This is my individual repository. It contains the dashboard page I built,
the data behind it, the code used to clean and prepare that data, and my
three internship artifact files.

The application is built with Python (Pandas, NumPy) and Streamlit, with
Plotly for the charts.

---

## Folder structure

```
├── dashboards/
│   └── 4_Health_Programs_Population_Vulnerability.py
├── data/
│   ├── fact_health_programs_cleaned.csv
│   ├── fact_disease_surveillance_cleaned.csv
│   ├── fact_environmental_cleaned.csv
│   ├── fact_lab_healthcare_cleaned.csv
│   ├── fact_outbreak_cleaned.csv
│   ├── dim_program_cleaned.csv
│   ├── dim_state_cleaned.csv
│   ├── dim_dates_cleaned.csv
│   ├── dim_disease_cleaned.csv
│   └── dim_source_cleaned.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py                   cached loading and table joins
│   ├── filters.py                       sidebar filter panel
│   ├── geographic.py                    geographic helper functions
│   ├── kpis.py                          KPI calculation and formatting
│   └── styling.py                       shared styling and components
├── Internship_artifacts/
│   ├── Agile_Template_v0.1_Samuel_Manoj_Pinipe.xlsx
│   ├── Unit_Test_Plan_v0.1_Samuel_Manoj_Pinipe.xlsx
│   └── Defect_Tracker_v0.1_Samuel_Manoj_Pinipe.xlsx
├── app.py                               entry point and navigation
├── requirements.txt
├── LICENSE
└── README.md
```

---

## How to run

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application opens at `http://localhost:8501`. Run the command from the
project folder so that `src` and `dashboards` can be imported.

---

## Data model

A star schema of one fact table and four dimension tables. The raw fact file
has 6,981 rows covering 32 states, 6 programmes and 36 months. After cleaning,
6,885 rows remain.

| Table | Rows | Grain |
|---|---|---|
| fact_health_programs_cleaned | 6,981 | one row per state, month and programme |
| dim_program_cleaned | 6 | one row per programme |
| dim_state_cleaned | 32 | one row per state |
| dim_dates_cleaned | 36 | one row per month |
| dim_source_cleaned | 6 | one row per source (not joined — no key in the fact table) |

The `data` folder also holds the cleaned fact tables for the other areas of
the wider project (disease surveillance, environmental, laboratory and
outbreak). My page reads only the health programme tables listed above.

---

## KPIs

| KPI | Calculation |
|---|---|
| Program Coverage | average of program_coverage_pct |
| People Screened | sum of people_screened |
| Beneficiaries Reached | sum of beneficiaries_reached |
| Maternal Health Beneficiaries | sum of maternal_health_beneficiaries |
| Child Immunization | sum of child_immunization_count |
| High-Risk Individuals | sum of high_risk_individuals |
| Chronic Disease Patients | sum of chronic_disease_patients |
| Health Vulnerability Index | average of health_vulnerability_index |

Very large counts are shown in short form (K, M, B) because a ten digit value
does not fit inside a card. The exact value is printed below each card and is
also shown on hover, so nothing is hidden.

---

## Visuals

1. Program coverage over time — line chart, one line per year.
2. People screened against beneficiaries reached — grouped bars by state.
3. Population split by state — stacked bars of children, adults and elderly.
4. High-risk population by state — treemap.
5. Composite health vulnerability index by state — bar chart.
6. Socioeconomic score against health vulnerability — bubble chart with the
   correlation printed below it.

---

## Filters

State, Year, Month and Programme, all in the sidebar. Every filter applies to
every KPI and every chart. `All` means no filter for that box. If a selection
returns no rows, the page shows a message instead of drawing empty charts.

---

## Data cleaning decisions

- Duplicate fact rows are removed before any calculation.
- Dimension tables are made unique on their id column, so the join does not
  increase the row count.
- Rows with negative counts are removed, since a count cannot be negative.
- Text and blank entries in number columns become missing values instead of
  breaking a chart.
- Children, adults and elderly repeat across all six programme rows for the
  same state and month, so they are read from a duplicate free table and
  averaged. Every other measure genuinely varies by programme and is summed.

---

## Known limitations

- The vulnerability visual is a bar chart, not a filled map. A map needs an
  India boundary file, which is not part of this dataset.
- There is no source filter. `dim_source_cleaned.csv` is provided, but the fact table
  has no source key to join on.
- Child immunization values look too large in the source data — a single
  state, month and programme row records around 8 to 12 million against a
  child population of about 13 million. The calculation is correct, but the
  column appears cumulative or wrongly scaled, so the figure should be
  confirmed before it is quoted.

---

## Internship artifacts

The `Internship_artifacts` folder holds my individually filled Agile Template,
Unit Test Plan and Defect Tracker, covering my work from the start of the
internship to the final submission.

---

## License

Released under the MIT License. See the LICENSE file.
