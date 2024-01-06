

def toggle_case(input_string):
    toggled_string = ""
    for char in input_string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char  # If it's not a letter, keep it unchanged
    return toggled_string

# Input string
input_string = input("Enter a string or sentence: ")

# Toggle the case and print the result
result = toggle_case(input_string)
print("Toggled case:", result)
