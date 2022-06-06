# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_in_file = letter.read()

for name in open("./Input/Names/invited_names.txt"):
    name_without_new_line = name.replace("\n", "")
    file_name = "letter_for_"+name+".txt"
    file_name_no_new_line = file_name.replace("\n", "")
    with open(f"./Output/ReadyToSend/{file_name_no_new_line}", "w") as file:
        letter_with_replaced_names = letter_in_file.replace("[name]", name_without_new_line)
        file.write(letter_with_replaced_names)

