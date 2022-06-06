# def reverse_number(num):
# str_num = str(num)
# num_list = []

# for number in str_num:
#     num_list.append(number)

#  num_list.sort(reverse=True)
# strings = [str(num) for num in num_list]
# a_string = "".join(strings)
# an_integer = int(a_string)

# return an_integer
import re


# def reverse_words_order_and_swap_cases(sentence):
#   # Write your code here
#  list=[]
# list = sentence.split(' ')
# list.reverse()
# count = len(list)
# word = ""
# for i in range(count):
#   word += list[i] + " "


# return str(word).swapcase()

def getTotalX(a, b):
    # Write your code here

    factor_a = []
    factor_b = []
    potential_numbers = []
    total_length = len(a + b)
    final_integers = []

    for i in range (1, 101):
        for number_a in a:
            if number_a % i == 0:
                factor_a.append(i)
        for number_b in b:
            if number_b % i == 0:
                factor_b.append(i)
        potential_numbers = factor_a + factor_b

    for numbers in potential_numbers:
        if potential_numbers.count(numbers) == total_length:
            final_integers.append(numbers)

    return len(set(final_integers))


print(getTotalX((2, 4), (16, 32, 96)))
