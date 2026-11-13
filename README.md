

\# Week 9 Class 5 – Drilling Telemetry Capstone



\## Project Overview



This project focuses on processing drilling telemetry data using Python. It reads well sensor records, validates the data, converts pressure and temperature measurements, and generates output reports.



\## Project Structure



```text

casptone\_5/

├── data/

│   └── drilling\_telemetry\_capstone.txt

├── src/

│   ├── telemetry\_capstone.py

│   └── data/

│       ├── cleaned\_telemetry.csv

│       ├── rejected\_records.csv

│       └── well\_summary.csv

└── tests/

&#x20;   └── test\_telemetry\_capstone.py

```



\## Features



\- Converts pressure from PSI to kPa.

\- Converts temperature from Fahrenheit to Celsius.

\- Validates telemetry records.

\- Separates accepted and rejected records.

\- Generates well summary reports.

\- Includes unit tests for conversion functions.



\## How to Run



From the repository root, run:



```bash

python casptone\_5/src/telemetry\_capstone.py

```



\## How to Run Tests



```bash

python -m unittest discover -s casptone\_5/tests -v

```



\## Test Results



\- Total tests: 2

\- Passed: 2

\- Failed: 0



\## Generated Output Files



\- `cleaned\_telemetry.csv`

\- `rejected\_records.csv`

\- `well\_summary.csv`



\## Limitations



The project performs basic telemetry data processing and validation. It does not currently include machine learning or real-time monitoring.



\## Author



Ismail Aliyu Umar



