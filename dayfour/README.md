
# Week 9 Class 4 - Telemetry Parser

## Project Overview

This project reads synthetic drilling telemetry records, validates the data, converts pressure and temperature units, and exports valid records into a cleaned CSV file.

## Files
- student_telemetry_parser.py: Main telemetry parser.
- test_student_telemetry_parser.py: Automated unit tests.
- drilling_telemetry_raw.txt: Original synthetic input records.
- validated_telemetry.csv: Cleaned output file.

## Results
- Total data records: 12
- Accepted records: 6
- Rejected records: 6
- Unit tests passed: 6
- Unit tests failed: 0

## How to Run

Run the parser:

    python student_telemetry_parser.py

Run the tests:

    python -m unittest discover -v

## Validation

Invalid records are rejected with their original source line numbers and descriptive error messages. Valid records are converted into kPa and Celsius and saved using the required CSV columns.
