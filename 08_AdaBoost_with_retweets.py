from twitterscraper import query_tweets_from_user
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.ensemble import AdaBoostClassifier
sid = SentimentIntensityAnalyzer()
model=AdaBoostClassifier()

features = []
labels = []

all_tweets = query_tweets_from_user("barackobama", limit=800)

training = all_tweets[:600]
testing = all_tweets[600:]

for tweet in training:
	tweetAnalysis = sid.polarity_scores(tweet.text)
	features.append([int(tweetAnalysis["neg"]*100),int(tweetAnalysis["pos"]*100),int(tweetAnalysis["neu"]*100),int(tweet.retweets/1000)])
	labels.append(int(tweet.likes/1000))

model = model.fit(features,labels)

matches = 0
errors = 0
for test in testing:	
	print("Real:")
	real = int(test.likes/1000)
	print(real)
	print("Prediction")
	tweetAnalysis = sid.polarity_scores(test.text)
	feature = [[int(tweetAnalysis["neg"]*100),int(tweetAnalysis["pos"]*100),int(tweetAnalysis["neu"]*100),int(test.retweets/1000)]]
	predict = model.predict(feature)
	if real -1 <= predict <= real+1:
		matches += 1
	else:
		errors += 1
	

print("matches")
print(matches)
print("errors")
print(errors)
