

# Charlotte Week 9 – Class 2 Homework

## Python Collections and Drilling Telemetry

**Student:** Ismail Aliyu Umar  
**Training:** Charlotte Data Analytics and Machine Learning Training  
**Module:** Python – Week 9, Class 2

## Part A – Concept Questions

**1. Difference between a list and a tuple**

A list is a collection that can be modified after it is created, while a tuple cannot be modified. For example, pressure readings that may change can be stored in a list, while fixed well coordinates can be stored in a tuple.

**2. Why are dictionary keys useful?**

Dictionary keys help identify the meaning of each value. For example, in a sensor observation, `pressure` identifies the pressure reading, while `temperature` identifies the temperature reading.

**3. What is zero-based indexing?**

Zero-based indexing means that Python starts counting positions from zero. For example, `readings[0]` selects the first item, while `readings[-1]` selects the last item.

**4. Observation count versus unique well count**

Observation count is the total number of recorded observations, including repeated well IDs. Unique well count is the number of different wells represented in those observations.

**5. What does a set do with duplicate IDs?**

A set removes duplicate values and keeps only one occurrence of each value. It is useful for identifying unique well IDs.

**6. Why is `sorted()` useful with a set?**

A set does not guarantee a particular order. The `sorted()` function arranges its values in ascending order, making them easier to read and compare.

**7. What happens when a dictionary has duplicate keys?**

If the same key appears more than once in a dictionary literal, the last value assigned to that key replaces the earlier value.

**8. Difference between `.get()` and square brackets**

The `.get()` method returns `None` or a specified default value when a key is missing. Square brackets raise a `KeyError` when the requested key does not exist.

## Part C – Reflection

### Why a list of dictionaries is useful for sensor observations

A list of dictionaries is useful for storing drilling sensor observations because each observation can contain different information such as well ID, pressure, temperature and sensor status. The list allows us to store many observations, even when they come from the same well. Each dictionary represents one observation, while the list keeps all the observations together. This is important because a well can have several readings taken at different times. If we used a dictionary with well IDs as keys, repeated well IDs could overwrite earlier observations. Using a list of dictionaries therefore helps preserve the recorded data and makes it easier to analyse changes in well conditions.

