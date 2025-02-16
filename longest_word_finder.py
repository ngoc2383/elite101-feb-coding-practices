# Return the first word if there's multiple words of the same length
# Punctuation is INCLUDED in the word 

def find_longest_word():
    sentence = input("Your sentence: ") # Get the user input
    longest = "" # Set initial longest word to be 0 length
    for word in sentence.split(): 
        if len(word) > len(longest):
            longest = word # If the word is longer than the CURRENT longest, word becomes the longest
    return longest

print(f'The longest word is: {find_longest_word()}') # Print the result