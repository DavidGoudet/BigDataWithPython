from twitterscraper import query_tweets_from_user
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.linear_model import LinearRegression

sid = SentimentIntensityAnalyzer()
model=LinearRegression()

features = []
labels = []

#Aumentamos el número de tweets
all_tweets = query_tweets_from_user("barackobama", limit=800)

#Ahora entrenamos con 600 tweets
training = all_tweets[:600]
testing = all_tweets[600:]

for tweet in training:
	tweetAnalysis = sid.polarity_scores(tweet.text)
	#Dividimos el número de retweets y likes entre 1000 y lo convertimos en entero, para que ahora 30.000 y 30.500 ambos sean 30
	#Multiplicamos las probabilidades para trabajar con números más grandes, ahora 0.10 será 10
	features.append([int(tweetAnalysis["neg"]*100),int(tweetAnalysis["pos"]*100),int(tweetAnalysis["neu"]*100)])
	labels.append(int(tweet.likes/1000))

model = model.fit(features,labels)

#Además ahora con matches y errors vamos contando cuántos errores tenemos y cuántas veces acertamos la predicción (con un rango de más o menos 1000 de error)
matches = 0
errors = 0
for test in testing:	
	print("Real:")
	real = int(test.likes/1000)
	print(real)
	print("Prediction")
	tweetAnalysis = sid.polarity_scores(test.text)
	feature = [[int(tweetAnalysis["neg"]*100),int(tweetAnalysis["pos"]*100),int(tweetAnalysis["pos"]*100)]]
	predict = model.predict(feature)
	if real -1 <= predict <= real+1:
		matches += 1
	else:
		errors += 1
	

print("matches")
print(matches)
print("errors")
print(errors)
