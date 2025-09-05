
<img width="829" height="597" alt="image" src="https://github.com/user-attachments/assets/9bf6c24e-c8c9-4380-9c73-798a1947d4e1" />

# Twitter Sentiment Analysis

A web-based application for performing **Sentiment Analysis on Tweets** using the **Twitter/X API**, `Tweepy`, and `scikit-learn`.  
The app is built with **Streamlit**, allowing users to interactively fetch tweets and analyze their sentiment in real time.



>> Features

- Fetch recent tweets from a given username using the **Twitter API (v2)**.
- Perform **sentiment classification** (Positive / Negative / Neutral).
- Clean and preprocess tweets using **NLTK**.
- Visualize results interactively in **Streamlit**.
- Fallback to local JSON/CSV data for offline testing (avoiding API rate limits).



>> Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [Tweepy](https://www.tweepy.org/) – Twitter API wrapper
- [scikit-learn](https://scikit-learn.org/stable/)
- [NLTK](https://www.nltk.org/)



>> Installation
1. Clone the repository:

git clone https://github.com/your-username/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis

2.Create a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate    # On Windows

OR

source venv/bin/activate # On Mac/Linux

3.Install dependencies:

pip install -r requirements.txt

>>Dataset

This project uses the **Sentiment140 dataset** for training the sentiment analysis model.  
Due to its large size, the dataset is **not included in this repository**.

>>> How to get the dataset:
- Official link: [Sentiment140 Dataset](http://help.sentiment140.com/for-students)  
- Direct Kaggle link: [Twitter Sentiment140 on Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)  

>>> Instructions:
1. Download the dataset CSV file (`training.1600000.processed.noemoticon.csv`) from Kaggle or the official site.  
2. Place the file in the `data/` folder of this project (create it if it doesn’t exist):
    project-root/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── data/
└── training.1600000.processed.noemoticon.csv
3. Update the dataset path in `app.py` if necessary.

> ⚠️ Note: The dataset is **1.6 million tweets (~200MB)**, so downloading may take a few minutes.



>> Setup Twitter API

Create a Twitter Developer Account.
Generate a Bearer Token in your Project/App.
Add it to your environment variables:

setx BEARER_TOKEN "your_token_here"   # On Windows

export BEARER_TOKEN="your_token_here" # On Mac/Linux

>> Run the App

streamlit run app.py

Then open http://localhost:8501 in your browser.

>> Example Output

Enter a Twitter username (e.g., JeffBezos).
The app fetches recent tweets.
Each tweet is classified as Positive, Negative, or Neutral.
Results are displayed interactively.

>> API Limits

Free-tier API only allows 100 tweets/month.
To avoid hitting the limit, the app supports saving tweets locally (tweets.json) and reusing them for testing.

>> Future Improvements

Support more advanced ML models (BERT, RoBERTa).

Integrate real-time streaming with WebSockets.

Improve visualization with word clouds and graphs.

>> License

This project is licensed under the MIT License – feel free to use and modify it.

