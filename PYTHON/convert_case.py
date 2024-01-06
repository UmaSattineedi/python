def convert_case(input_string):
    converted_string = ""

    for char in input_string:
        if char.isupper():
            converted_string += char.lower()
        elif char.islower():
            converted_string += char.upper()
        else:
            converted_string += char  # If character is not a letter, keep it unchanged

    return converted_string

# Input string or sentence
input_text = input("Enter a string or sentence: ")

# Convert case and print the result
result = convert_case(input_text)
print("Converted string:", result)


