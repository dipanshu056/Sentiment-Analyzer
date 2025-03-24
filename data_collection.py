import pandas as pd

# Manual sample data 
data = [
    {"text": "I love this place", "sentiment": "positive"},
    {"text": "This is terrible", "sentiment": "negative"},
    {"text": "I love this app!", "sentiment": "positive"},
    {"text": "Worst experience ever", "sentiment": "negative"},
    {"text": "It's okay", "sentiment": "neutral"}
]
df = pd.DataFrame(data)
df.to_csv('data/sample_tweets.csv', index=False)
print("Sample data saved to data/sample_tweets.csv")
