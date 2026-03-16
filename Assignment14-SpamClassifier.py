import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
data = {
    "Message": [
        "Win a free lottery now",
        "Hello how are you",
        "Claim your free prize",
        "Let's meet tomorrow",
        "Exclusive offer just for you"
    ],
    "Label": ["Spam", "Ham", "Spam", "Ham", "Spam"]
}

df = pd.DataFrame(data)

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Message"])

# Labels
y = df["Label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Test message
new_message = ["Free prize waiting for you"]
new_data = vectorizer.transform(new_message)

prediction = model.predict(new_data)

print("Message:", new_message[0])
print("Prediction:", prediction[0])

'''
Spam Detection System Design
1. Features (Input Data for Model)
Features are the characteristics used by the machine learning model to detect spam messages.
Some important features include:
Message text content
Presence of spam keywords (e.g., "free", "win", "offer", "lottery")
Number of links in the message
Sender email address or phone number
Message length
Use of capital letters or special characters
These features help the model identify patterns commonly found in spam messages.

2. Data Needed

To train a spam detection system, a dataset containing two types of messages is required:

Spam Messages – Promotional or unwanted messages such as advertisements or scams.

Ham Messages – Normal messages that are not spam.

Each message in the dataset should be labeled as either Spam or Not Spam so that the machine learning model can learn the difference between them.

Example Dataset Structure:

Message	Label
"Congratulations! You won a prize"	Spam
"Are we meeting tomorrow?"	Not Spam
3. Possible Mistakes (Errors)

A spam classifier can make two types of mistakes:

1. False Positive
A normal message is wrongly classified as spam.
Example: A real promotional message from a trusted store goes to the spam folder.

2. False Negative
A spam message is wrongly classified as a normal message.
Example: A scam message appears in the inbox.

These mistakes can affect the reliability of the spam detection system.
'''