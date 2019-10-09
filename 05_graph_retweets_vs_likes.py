#Part of a Course from Hezion Studios on Big Data: Trinity

#Importamos matploblib, que nos permitirá hacer el gráfico (Funciona en Repl.it)
import matplotlib.pyplot as plt
from twitterscraper import query_tweets_from_user

retweets = []
likes = []

all_tweets = (query_tweets_from_user("barackobama", limit=100))

for tweet in all_tweets:
    retweets.append(tweet.retweets)
    likes.append(tweet.likes)

#Imprimimos un gráfico de retweets vs likes
plt.plot(retweets, likes, 'o-')
plt.show()
plt.savefig("retweetslikes.png")
