
# Week 9 Class 3 Student Lab
# Control Flow and Functions

# Section A: Decisions

def classify_pressure(pressure_psi):
    if pressure_psi is None or pressure_psi < 0:
        return "invalid"
    elif pressure_psi >= 3500:
        return "high"
    elif pressure_psi >= 2500:
        return "normal"
    else:
        return "low"


# Section B: Loops

READINGS = [
    {"well_id": "WELL-07", "pressure_psi": 3150, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2780, "status": "active"},
    {"well_id": "WELL-09", "pressure_psi": 3325, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": 2895, "status": "active"},
    {"well_id": "WELL-07", "pressure_psi": 3210, "status": "active"},
    {"well_id": "WELL-11", "pressure_psi": None, "status": "invalid"},
    {"well_id": "WELL-08", "pressure_psi": 2810, "status": "active"},
    {"well_id": "WELL-12", "pressure_psi": 2715, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": 4100, "status": "active"},
    {"well_id": "WELL-13", "pressure_psi": -25, "status": "active"}
]

print("SECTION B: ALL PRESSURE CLASSIFICATIONS")

for reading in READINGS:
    well_id = reading["well_id"]
    pressure = reading["pressure_psi"]
    classification = classify_pressure(pressure)

    print(well_id, pressure, classification)


# Section C: Functions

def psi_to_kpa(pressure_psi):
    if pressure_psi is None or pressure_psi < 0:
        return None
    return pressure_psi * 6.8947572932


converted_pressure = psi_to_kpa(3150)

print("\nSECTION C: PRESSURE CONVERSION")
print("3150 psi in kPa is", round(converted_pressure, 2))


# Section D: Filter and Summarize

totals = {}
counts = {}
skipped = 0
valid = 0

for reading in READINGS:
    well_id = reading["well_id"]
    pressure = reading["pressure_psi"]

    if reading["status"] != "active":
        skipped += 1
        continue

    if pressure is None or pressure < 0:
        skipped += 1
        continue

    valid += 1

    if well_id not in totals:
        totals[well_id] = 0
        counts[well_id] = 0

    totals[well_id] += pressure
    counts[well_id] += 1


print("\nSECTION D: SUMMARY")

print("Valid readings:", valid)
print("Skipped readings:", skipped)

for well_id in totals:
    average = totals[well_id] / counts[well_id]
    print(well_id, "average pressure:", round(average, 2), "psi")


# Section A: Boundary Checks

print("\nBOUNDARY CHECKS")

test_values = [None, -1, 0, 2499, 2500, 3499, 3500]

for value in test_values:
    print(value, classify_pressure(value))
