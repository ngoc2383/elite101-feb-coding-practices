# Return the first word if there's multiple words of the same length
# Punctuation is INCLUDED in the word 

def find_longest_word():
    sentence = input("Your sentence: ")
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):
            longest = word
    return longest

print(f'The longest word is: {find_longest_word()}')