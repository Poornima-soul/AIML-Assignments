from textblob import TextBlob

# 5 sample reviews
reviews = [
    "This movie is amazing and very interesting",
    "Worst movie I have ever seen",
    "The film was okay, not bad",
    "I loved the acting and story",
    "It was boring and too long"
]

# Analyze sentiment
for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Review:", review)
    print("Sentiment:", sentiment)
    print()