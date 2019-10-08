#Part of a Course from Hezion Studios on Big Data: Trinity

from sklearn.neural_network import MLPClassifier

features = [[4,1],[4,0],[2,0],[3,0],[4,0]]
labels = [0,0,1,1,0]
mlp = MLPClassifier(hidden_layer_sizes=(10,10))
mlp = mlp.fit(features,labels)

print(mlp.predict([[5,1]]))
