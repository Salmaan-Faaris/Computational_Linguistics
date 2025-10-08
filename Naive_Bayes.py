import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import string

data = {
    'text': [
        "I love this movie, it was fantastic!",
        "This film was horrible and boring.",
        "What a great experience, truly inspiring.",
        "I hated every moment of it.",
        "The actors did a wonderful job.",
        "Terrible plot and weak acting.",
        "Absolutely loved the cinematography.",
        "It was okay, not the best.",
        "Worst movie ever!",
        "An enjoyable and heartwarming film.",
        "I really enjoyed the movie.",
        "The film was too long and dull.",
        "I really hated this movie, it was awful.",
        "Such a wonderful and emotional story.",
        "Boring from start to finish.",
        "One of the best movies I’ve seen!",
        "The script was weak and predictable."
    ],
    'sentiment': ['positive', 'negative', 'positive', 'negative', 'positive',
        'negative', 'positive', 'neutral', 'negative', 'positive','positive',
        'negative','negative', 'positive', 'negative', 'positive', 'negative']
}
df = pd.DataFrame(data)

def clean_text(text):
    text = text.lower()  
    text = ''.join(ch for ch in text if ch not in string.punctuation)
    return text

df['text'] = df['text'].apply(clean_text)



X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['sentiment'], test_size=0.2, random_state=42
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_vec, y_train)
y_pred = model.predict(X_test_vec)

sample_reviews = [
    "I really enjoyed the movie",
    "The film was too long and dull.",
    "Boring film."
]

sample_vec = vectorizer.transform(sample_reviews)
predictions = model.predict(sample_vec)

for review, sentiment in zip(sample_reviews, predictions):
    print(f"Review: {review}\nPredicted Sentiment: {sentiment}\n")
