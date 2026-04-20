from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents
documents = [
    "Machine learning is fun and useful",
    "Machine learning makes systems intelligent",
    "Artificial intelligence and machine learning are related",
    "Deep learning is a branch of machine learning",
    "AI is transforming the future"
]

# Apply TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Get feature names
features = vectorizer.get_feature_names_out()

# Display top keywords for each document
for i in range(len(documents)):
    print("\nDocument", i + 1)
    scores = X[i].toarray()[0]
    word_scores = list(zip(features, scores))

    # Sort by highest score
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)

    # Print top 3 keywords
    for word, score in sorted_words[:3]:
        print(word, ":", round(score, 2))


'''''
Explanation

TF-IDF (Term Frequency–Inverse Document Frequency) is used to find important words in a document.

Words that appear frequently in one document get higher scores
Words that appear in many documents get lower scores

For example:

Words like “machine” and “learning” appear in many documents → lower importance
Words like “fun”, “intelligent”, “future” appear in fewer documents → higher importance

TF-IDF helps in identifying key terms or keywords from text data. It is widely used in search engines, text analysis, and NLP applications to extract meaningful information from documents.
'''''