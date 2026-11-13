
"""Week 9 Class 4 STUDENT LAB
Input is synthetic training data; do not change supplied source log.
"""
from pathlib import Path
from datetime import datetime
import csv
import math

PSI_TO_KPA = 6.8947572932


def parse_line(line: str) -> dict:
    """Return normalized record with well_id, timestamp, pressure_kpa,
    temperature_c and status. Raise ValueError on invalid rows.
    """
    parts = [part.strip() for part in line.strip().split("|")]

    if len(parts) != 7:
        raise ValueError("Expected exactly seven fields")

    well_id, stamp, p_text, p_unit, t_text, t_unit, status = parts

    if not well_id:
        raise ValueError("Well ID is missing")

    try:
        datetime.fromisoformat(stamp)
    except ValueError:
        raise ValueError("Invalid ISO timestamp")

    try:
        pressure = float(p_text)
        temperature = float(t_text)
    except ValueError:
        raise ValueError("Pressure and temperature must be numeric")

    if not math.isfinite(pressure) or pressure < 0:
        raise ValueError("Pressure must be finite and non-negative")

    if not math.isfinite(temperature):
        raise ValueError("Temperature must be finite")

    if p_unit.lower() == "psi":
        pressure_kpa = pressure * PSI_TO_KPA
    elif p_unit.lower() == "kpa":
        pressure_kpa = pressure
    else:
        raise ValueError("Unsupported pressure unit")

    if t_unit.upper() == "F":
        temperature_c = (temperature - 32) * 5 / 9
    elif t_unit.upper() == "C":
        temperature_c = temperature
    else:
        raise ValueError("Unsupported temperature unit")

    status = status.upper()

    if status not in ("ACTIVE", "OFFLINE"):
        raise ValueError("Invalid status")

    return {
        "well_id": well_id,
        "timestamp": stamp,
        "pressure_kpa": round(pressure_kpa, 2),
        "temperature_c": round(temperature_c, 2),
        "status": status
    }


def process_log(source: Path, output: Path) -> tuple[int, list[tuple[int, str]]]:
    """Read source text, skip comments, save valid rows as CSV, report rejected rows."""
    records = []
    rejected = []

    with open(source, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):

            if not line.strip() or line.lstrip().startswith("#"):
                continue

            try:
                record = parse_line(line)
                records.append(record)

            except ValueError as error:
                rejected.append((line_number, str(error)))

    with open(output, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "well_id",
            "timestamp",
            "pressure_kpa",
            "temperature_c",
            "status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return len(records), rejected


if __name__ == "__main__":
    root = Path(__file__).resolve().parent

    accepted, errors = process_log(
        root / "drilling_telemetry_raw.txt",
        root / "validated_telemetry.csv"
    )

    print("Accepted:", accepted)
    print("Rejected:", len(errors))

    for number, message in errors:
        print("Line", number, ":", message)
