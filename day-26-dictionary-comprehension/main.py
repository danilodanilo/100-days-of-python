# new_dict = {new_key:new_value for (key, value) in list}
# or
# directly from a existing dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
#
# passed_students = {student: score for (student, score) in students_score.items() if score >= 50}
# print(passed_students)

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)
import pandas
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each
# temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {week_day: ((temp_c * 9/5) + 32) for (week_day, temp_c) in weather_c.items()}
print(weather_f)