well_id = "WELL-001"
pressure_psi = 3000.0
temperature_f = 32.0
sensor_active = True

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f - 32) * 5.0/9.0

print('the well identifier is', well_id)
print('the pressure in kPa is', round(pressure_kpa, 1))
print('the temperature in Celsius is', round(temperature_c, 1))
print('the sensor status is', sensor_active)

raw_pressure = "3150"
conversion_factor = 6.89476

# pressure_kpa = raw_pressure * conversion_factor
pressure_kpa = float(raw_pressure) * conversion_factor
print('the converted pressure is', round(pressure_kpa, 1))