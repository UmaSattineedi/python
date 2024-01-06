def get_second_to_last_word(sentence):
    words = sentence.split()
    
    # Ensure the sentence has at least two words
    if len(words) < 2:
        return "Sentence should have at least two words."

    second_to_last_word = words[-2]
    return second_to_last_word

# Input sentence
input_sentence = input("Enter a sentence: ")

# Get the second-to-last word and print it
result = get_second_to_last_word(input_sentence)
print("Second-to-last word:", result)
