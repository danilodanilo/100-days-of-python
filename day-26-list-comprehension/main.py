# for string
# name = input("Type your name ")
# newstring = [letter for letter in name]
# print(newstring)

# for a list
# numbers = [1, 2, 3]
# newlist = [n+1 for n in numbers]
# print(newlist)

# challenge - create a new list from a range, where items are double the values in the range
# values = [n*2 for n in range(1, 5)]
# print(values)


# other things that can be done with list comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# return the names that have only 4 letters
# short_names = [name for name in names if len(name) == 4]
# return the names in capital letters for names that have more than 5 letters
# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)

# create a new list from a list of numbers that have the squared numbers of the list of numbers
# list_of_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_list_of_numbers = [number * number for number in list_of_numbers]
# print(squared_list_of_numbers)

# This new list should only contain the even numbers from the list numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [number for number in numbers if number % 2 == 0]
# print(result)

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]

print(result)


