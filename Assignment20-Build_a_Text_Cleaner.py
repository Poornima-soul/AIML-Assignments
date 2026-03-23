import string

# Define stopwords
stopwords = ["is", "a", "the", "and", "to", "of", "in", "on", "for"]


def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")

    # Remove stopwords
    words = text.split()
    cleaned_words = []

    for word in words:
        if word not in stopwords:
            cleaned_words.append(word)

    return " ".join(cleaned_words)


# Test the program
text = input("Enter a sentence: ")
print("Cleaned Text:", clean_text(text))