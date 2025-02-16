# No punctuation, short words not included, and all caps
# Example: Random Access Memory -> RAM

def acronym_generator(phrase):
    words = phrase.split() # Split the phrase into a list of words
    acronym = []
    # Loop through each word in the phrase
    for word in words:
        # Check if the word is greater than 3 characters and is a letter (no punctuation)
        if len(word) > 3 and word.isalpha():
            acronym.append(word[0].upper()) # Append the capitalized first letter
    return ''.join(acronym) # Join the list into a string


print(acronym_generator('National Aeronautics Space Administration'))  # NASA