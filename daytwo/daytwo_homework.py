# Eight oil well sensor observations

observations = [
    {
        'well_id': 'WELL-07',
        'pressure': 3150,
        'temperature': 186,
        'sensor_active': True
    },
       {
        'well_id': 'WELL-08',
        'pressure': 2780,
        'temperature': 172,
        'sensor_active': False
    },
       {
        'well_id': 'WELL-07',
        'pressure': 3325,
        'temperature': 195,
        'sensor_active': True
    },
       {
        'well_id': 'WELL-08',
        'pressure': 2890,
        'temperature': 180,
        'sensor_active': False
    },
       {
        'well_id': 'WELL-07',
        'pressure': 3040,
        'temperature': 188,
        'sensor_active': True
    },
       {
        'well_id': 'WELL-08',
        'pressure': 3180,
        'temperature': 187,
        'sensor_active': False
    },
       {
        'well_id': 'WELL-07',
        'pressure': 2510,
        'temperature': 166,
        'sensor_active': True
    },
       {
        'well_id': 'WELL-08',
        'pressure': 2815,
        'temperature': 174,
        'sensor_active': False
    }
]

# Display the first two observations

print(observations[0:2])

# Display the last observation

print(observations[-1])

well_ids = []

for well_observation in observations:
    well_ids.append(well_observation['well_id'])

print(well_ids)

unique_wells = set(well_ids)

print(unique_wells)

sorted_wells = sorted(unique_wells)

print(sorted_wells)

# Display observation fields

print(observations[0].keys())

# Display sorted observation fields
sorted_fields = sorted(observations[0].keys())

print(sorted_fields)

# Collect pressure readings from all observations

pressure_readings = []

for well_observation in observations:
    pressure_readings.append(well_observation['pressure'])
    print(pressure_readings)

    # Calculate total and average pressure

total_pressure = sum(pressure_readings)

average_pressure = total_pressure / len(pressure_readings)

print("Total pressure (psi):", total_pressure)
print("Average pressure (psi):", average_pressure)

# Count observations for each well

well_observation_count = {}

for well_observation in observations:
    well_id = well_observation['well_id']

    if well_id in well_observation_count:
        well_observation_count[well_id] = well_observation_count[well_id] + 1
    else:
        well_observation_count[well_id] = 1

print("Observations per well:", well_observation_count)