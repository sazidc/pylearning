# Exercise 1 - Dictionary Comprehension

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Exercise 2 - Dictionary Comprehension

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)