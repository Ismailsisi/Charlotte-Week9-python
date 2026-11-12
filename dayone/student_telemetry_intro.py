# Sample telemetry data for WELL-07

well_id = "WELL-07"
raw_pressure = "3150.0"
raw_temperature = "186.0"
sensor_active = True

# Convert raw sensor readings into numbers

raw_pressure = "3150.0"
raw_temperature = "186.0"

pressure_psi = float(raw_pressure)
temperature_f = float(raw_temperature)

# Convert pressure and temperature units

pressure_kpa = pressure_psi * 6.8947572932
temperature_c = (temperature_f - 32) * 5 / 9

# Display telemetry report

print(f"Well ID: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor active: {sensor_active}")

