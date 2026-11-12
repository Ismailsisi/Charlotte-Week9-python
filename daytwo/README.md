# Class 2 Lab Reflection: Python Collections

## Introduction
In this practical, I worked with Python collections to organize and analyse multi-well sensor readings. The dataset contained eight observations from six different wells.

## What I Learned

**1. Lists**

I used a list to store all the well observations. A list was useful because it keeps the readings in order and allows repeated observations from the same well.

**2. Dictionaries**

I used dictionaries to store information in key-value pairs, such as well IDs, pressure readings, temperature readings and sensor status. I also used a dictionary to count the number of observations for each well.

**3. Sets**

I used sets to identify unique well IDs and field names. Sets automatically remove duplicates, which helped me identify six distinct wells from the eight observations.

**4. Tuples**

I used a tuple to store measurement units such as psi and Fahrenheit. A tuple was suitable because these values were not expected to change during the exercise.

## Practical Results

- Total observations: 8
- Unique wells: 6
- Distinct fields: East, North and South
- Inactive sensor observations: 2
- Average pressure: 2961.25 psi
- Second WELL-07 observation pressure: 3180.0 psi

## Conclusion

This practical helped me understand how different Python collections can be used to organize and analyse sensor data. I also learned how to access values, identify duplicates, count observations and calculate average pressure using Python.