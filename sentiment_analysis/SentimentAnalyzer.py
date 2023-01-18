from typing import List

from pandas import DataFrame
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax


class SentimentAnalyzer:
    def __init__(self, twitter_data: DataFrame):
        self._twitter_data = twitter_data.loc[:, 'Tweet']
        self._roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        self._model = AutoModelForSequenceClassification.from_pretrained(self._roberta)
        self._tokenizer = AutoTokenizer.from_pretrained(self._roberta)
        self._labels = ['Negative', 'Neutral', 'Positive']

    def analyze_tweets_sentiment(self) -> List[str]:
        sentiment_results_column = []
        for tweet_content in self._twitter_data:
            prepared_tweet = self._prepare_words(tweet_content)
            tweet_sentiment_scores = self._analyze_sentiment(prepared_tweet)
            sentiment_result = self._prepare_result(tweet_sentiment_scores)
            sentiment_results_column.append(sentiment_result)
        return sentiment_results_column

    @staticmethod
    def _prepare_words(tweet_content: str) -> str:
        tweet_words = []
        for word in tweet_content.split(' '):
            if word.startswith('@') and len(word) > 1:
                word = '@user'
            elif word.startswith('http'):
                word = "http"
            tweet_words.append(word)
        prepared_tweet = " ".join(tweet_words)
        return prepared_tweet

    def _analyze_sentiment(self, prepared_tweet_content: str) -> List[str]:
        encoded_tweet = self._tokenizer(prepared_tweet_content, return_tensors='pt')
        output = self._model(**encoded_tweet)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        return scores

    def _prepare_result(self, sentiment_scores: List[str]) -> str:
        dictor = {}
        for i in range(len(sentiment_scores)):
            dictor[self._labels[i]] = sentiment_scores[i]
        return max(dictor, key=dictor.get)

