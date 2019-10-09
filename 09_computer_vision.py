#Part of a Course from Hezion Studios on Big Data: Trinity

#Importamos las bibliotecas
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image as Image
import random

#La siguiente es la dirección de Mobilenet
classifier_url ="https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"

#Definimos el número de pixeles que tendrá cada una de nuestras imágenes
IMAGE_SHAPE = (224, 224)

#Lo que hacemos a continuación es inicializar nuestra red neuronal usando el clasificador Mobilenet
#Sequential está recibiendo una lista de KerasLayers basados en el clasificador, un layer no es más que una columna de nuestra red neuronal
#Usamos input_shape para decirle que el número de entradas es función de la cantidad de pixeles de la imagen, porque la entrada de la red es una imagen
classifier = tf.keras.Sequential([
    hub.KerasLayer(classifier_url, input_shape=IMAGE_SHAPE+(3,))
])

#Generamos un número aleatorio simplemente para darle nombre aleatorio al archivo que se guardará con la imagen
#Esto es porque se queda en la caché y cada vez que probemos una nueva imagen queremos que use otro nombre para guardar, de otra forma usaremos la misma
random_number = random.random() * 100
image_url = 'https://images1.autocasion.com/actualidad/wp-content/uploads/2018/12/Ford-Ranger_Raptor-2019-1024-04.jpg'

#Cargamos la imagen desde la url con Keras y Pillow
image = tf.keras.utils.get_file(str(random_number)+".jpg", image_url)
image = Image.open(image).resize(IMAGE_SHAPE)

#La convertimos en un arreglo de números con NumPy, simplemente tomando sus pixeles y convirtiéndolos en números
image = np.array(image)/255.0
image.shape

#Hacemos la predicción, con nuestro clasificador previamente entrenado
result = classifier.predict(image[np.newaxis, ...])
result.shape

#Mobilenet puede reconocer 1000 tipos distintos de objetos, el resultado de la predicción es un arreglo con las probabilidades de que nuestra imagen contenga uno de esos objetos
array_of_results = result [0]

#Ordenamos el arreglo para tener primero el objeto con mayor probabilidad de estar en la imagen
sort = np.argsort(-array_of_results)
sorted_results = array_of_results[sort]

#Extraemos los ids (número de identificación) de los 3 objetos más probables
first_class = np.where(array_of_results == sorted_results[0])[0][0]
second_class = np.where(array_of_results == sorted_results[1])[0][0]
third_class = np.where(array_of_results == sorted_results[2])[0][0]

#En la lista ImageNetLabels.txt se encuentran los 1000 nombres de los objetos que el programa predice
labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())

#Imprimimos el resultado
first_class_name = imagenet_labels[first_class]
second_predicted_class_name = imagenet_labels[second_class]
third_predicted_class_name = imagenet_labels[third_class]

print("Prediction: " + first_class_name.title())
print("Second Prediction: " + second_predicted_class_name.title())
print("Third Prediction: " + third_predicted_class_name.title())
