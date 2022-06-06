from builtins import set

import pandas

# student_dictionary = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# students_data_frame = pandas.DataFrame(student_dictionary)
#
# # print(students_data_frame)
#
# # loop through rows of a data frame
#
# for (index, row) in students_data_frame.iterrows():
#     # print(index)
#     # print(row)
#     # to access a column
#     print(row.student)
#     print(row.score)

# NATO challenge

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary_NATO = {row.letter: row.code for (letter, row) in data.iterrows()}

word = input("Enter a word: ").upper()
list_NATO = []
for letter in word:
    for (index, row) in data.iterrows():
        if letter == row.letter:
            list_NATO.append(row.code)

print(list_NATO)
# another way of doing the same as above
list_NATO2 = [dictionary_NATO[letter] for letter in word]
print(list_NATO2)
