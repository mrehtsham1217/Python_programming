PLACEHOLDER = "[name]"
with open("names.txt") as names_files:
    names = names_files.readlines()
    # print(names)

with open("letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_names)
        # print(new_letter)
        with open(f"Letter_for_{stripped_names}.txt", mode='w') as file:
            file.write(new_letter)
