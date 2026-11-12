
# Activity A: List exploration

readings = [
    {"well_id": "WELL-07", "pressure_psi": 3150.0, "temperature_f": 186.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-08", "pressure_psi": 2780.0, "temperature_f": 172.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-09", "pressure_psi": 3325.0, "temperature_f": 195.0, "sensor_active": False, "field": "north"},
    {"well_id": "WELL-10", "pressure_psi": 2890.0, "temperature_f": 180.0, "sensor_active": True, "field": "east"},
    {"well_id": "WELL-11", "pressure_psi": 3040.0, "temperature_f": 188.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-07", "pressure_psi": 3180.0, "temperature_f": 187.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-12", "pressure_psi": 2510.0, "temperature_f": 166.0, "sensor_active": False, "field": "east"},
    {"well_id": "WELL-08", "pressure_psi": 2815.0, "temperature_f": 174.0, "sensor_active": True, "field": "south"}
]

# Q6: Count all observations
print(len(readings))

# Q7: Display the first and last well IDs
print(readings[0]["well_id"])
print(readings[-1]["well_id"])

# Q8: Select and count the first three observations
first_three = readings[0:3]
print(first_three)
print(len(first_three))


# Activity B: Tuples and dictionaries

# Q10: Create a tuple of measurement units and access its values
measurement_units = ("psi", "Fahrenheit")
print(measurement_units[0])
print(measurement_units[1])

# Q11: Display the dictionary keys in the first observation
print(readings[0].keys())

# Q12: Access dictionary values and check for a missing key
print(readings[0]["pressure_psi"])
print(readings[0]["field"])
print(readings[0].get("depth_m", "not supplied"))


# Activity C: Sets and membership

# Q14: Create a set of unique well IDs
unique_wells = {reading["well_id"] for reading in readings}
print(len(unique_wells))

# Q15: Convert unique well IDs into a sorted list
sorted_wells = sorted(unique_wells)
print(sorted_wells)

# Q16: Create a sorted list of distinct field names
unique_fields = {reading["field"] for reading in readings}
sorted_fields = sorted(unique_fields)
print(sorted_fields)

# Q17: Check whether WELL-12 exists
print("WELL-12" in unique_wells)

# Q18: Calculate the average pressure
pressures = [reading["pressure_psi"] for reading in readings]
print(pressures)
print(sum(pressures) / len(pressures))

# Q19: Count inactive sensors
inactive_count = sum(reading["sensor_active"] == False for reading in readings)
print(inactive_count)

# Q20: Count observations for each well
well_counts = {}

for reading in readings:
    well_id = reading["well_id"]
    well_counts[well_id] = well_counts.get(well_id, 0) + 1

print(well_counts)

# Q21: Retrieve the pressure of the second WELL-07 observation
print(readings[5]["pressure_psi"])