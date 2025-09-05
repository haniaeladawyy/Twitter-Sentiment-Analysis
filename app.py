import tweepy
import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

# -------------------------
# Setup Twitter API
# -------------------------
BEARER_TOKEN = "YOUR_BEARER_TOKEN"  # ⚠️ Replace with your token or 
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# -------------------------
# Load stopwords and model
# -------------------------
@st.cache_resource
def load_stopwords():
    nltk.download('stopwords')
    return stopwords.words('english')

@st.cache_resource
def load_model_and_vectorizer():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# -------------------------
# Sentiment prediction
# -------------------------
def predict_sentiment(text, model, vectorizer, stop_words):
    text = re.sub('[^a-zA-Z]', ' ', text).lower().split()
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)
    text = vectorizer.transform([text])
    sentiment = model.predict(text)
    return "Negative" if sentiment == 0 else "Positive"

# -------------------------
# Get tweets using Tweepy
# -------------------------
def get_tweets(username, limit=5):
    try:
        user = client.get_user(username=username)
        tweets = client.get_users_tweets(id=user.data.id, max_results=limit)
        return [tweet.text for tweet in tweets.data]
    except Exception as e:
        st.error(f"Failed to fetch tweets: {e}")
        return []

# -------------------------
# Streamlit App
# -------------------------
def main():
    st.title("Twitter Sentiment Analysis (with API)")

    stop_words = load_stopwords()
    model, vectorizer = load_model_and_vectorizer()

    option = st.selectbox("Choose an option", ["Input text", "Get tweets from user"])

    if option == "Input text":
        text_input = st.text_area("Enter text to analyze sentiment")
        if st.button("Analyze"):
            sentiment = predict_sentiment(text_input, model, vectorizer, stop_words)
            st.write(f"Sentiment: {sentiment}")

    elif option == "Get tweets from user":
        username = st.text_input("Enter Twitter username")
        if st.button("Fetch Tweets"):
            tweets = get_tweets(username, limit=5)
            if tweets:
                for tweet_text in tweets:
                    sentiment = predict_sentiment(tweet_text, model, vectorizer, stop_words)
                    color = "green" if sentiment == "Positive" else "red"
                    st.markdown(
                        f"""
                        <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;">
                            <h5 style="color: white;">{sentiment} Sentiment</h5>
                            <p style="color: white;">{tweet_text}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                st.write("No tweets found.")

if __name__ == "__main__":
    main()
