#Importamos las bibliotecas que usaremos:
from twitterscraper import query_tweets_from_user
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.neural_network import MLPClassifier

#Inicializamos nuestro analizador de sentimientos
sid = SentimentIntensityAnalyzer()

#Hacemos una red neuronal simple, un Multi-layer Perceptron classifier con 3 columnas de neuronas, cada una con 10 neuronas
mlp = MLPClassifier(hidden_layer_sizes=(10,10,10))

features = []
labels = []

#Leemos 40 tweets de la cuenta de Obama
all_tweets = (query_tweets_from_user("barackobama", limit=40))

#Tomamos los 20 primeros tweets de Obama para entrenar a nuestra red neuronal, es decir, por cada tweet tenemos su sentimiento y su número de likes, buscaremos que la red neuronal, dado el sentimiento, nos devuelva el número de likes
training = all_tweets[:20]
#Los últimos 20 tweets los tomamos para hacer pruebas
testing = all_tweets[20:]

#Por cada tweet tomamos su sentimiento, que es un arreglo de tres números, por ejemplo: [0.1,0.2,0.8], que es la probabilidad de que el sentimiento sea negativo, positivo, o neutral. Por cada tweet vamos agregando a un arreglo llamado "features" su sentimiento y a un arreglo llamado "labels" su número de likes
for tweet in training:
	tweetAnalysis = sid.polarity_scores(tweet.text)
	features.append([tweetAnalysis["neg"],tweetAnalysis["pos"],tweetAnalysis["neu"]])
	labels.append(tweet.likes)

#Entrenamos a la red neuronal simplemente llamando a la función "fit"
mlp = mlp.fit(features,labels)

#Por cada tweet de la lista que habíamos hecho para probar, tratamos de predecir su número de likes usando nuestra red neuronal previamente entrenada. Imprimimos el número real de tweets y luego la predicción.
for test in testing:	
	print("Real:")
	print(test.likes)
	print("Prediction")
	tweetAnalysis = sid.polarity_scores(test.text)
	feature = [[tweetAnalysis["neg"],tweetAnalysis["pos"],tweetAnalysis["neu"]]]
	print(mlp.predict(feature))

