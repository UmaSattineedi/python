def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Input string
input_string = input("Enter a string: ")

# Reverse the string and print the result
result = reverse_string(input_string)
print("Reversed string:", result)
