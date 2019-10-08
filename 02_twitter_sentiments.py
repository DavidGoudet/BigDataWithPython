import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from twitterscraper import query_tweets

sid = SentimentIntensityAnalyzer()

def get_sentiment(tweet):
  tweetAnalysis = sid.polarity_scores(tweet)
  if tweetAnalysis['pos'] > tweetAnalysis['neg']: 
      return 'positive'
  else: 
      return 'negative'

for tweet in query_tweets("Joker", 10, poolsize=1)[:100] :    
    print("-----TWEET----")
    print(tweet.text)
    print(get_sentiment(tweet.text))
