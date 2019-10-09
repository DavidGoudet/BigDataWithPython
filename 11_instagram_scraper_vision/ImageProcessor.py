import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image as Image
import random

class ImageProcessor:
  IMAGE_SHAPE = (224, 224)

  def configureClassifier(self):
    classifier_url ="https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
    
    classifier = tf.keras.Sequential([
        hub.KerasLayer(classifier_url, input_shape=self.IMAGE_SHAPE+(3,))
    ])
    return classifier

  def predictImageObjects(self, image_url):
    classifier = self.configureClassifier()
    random_number = random.random() * 100
    
    image = tf.keras.utils.get_file(str(random_number)+".jpg", image_url)
    image = Image.open(image).resize(self.IMAGE_SHAPE)

    image = np.array(image)/255.0
    image.shape

    result = classifier.predict(image[np.newaxis, ...])
    result.shape

    array_of_results = result[0]

    sort = np.argsort(-array_of_results)
    sorted_results = array_of_results[sort]

    first_class = np.where(array_of_results == sorted_results[0])[0][0]
    second_class = np.where(array_of_results == sorted_results[1])[0][0]
    third_class = np.where(array_of_results == sorted_results[2])[0][0]

    labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
    imagenet_labels = np.array(open(labels_path).read().splitlines())

    first_class_name = imagenet_labels[first_class]
    second_predicted_class_name = imagenet_labels[second_class]
    third_predicted_class_name = imagenet_labels[third_class]

    return [first_class_name.title(), second_predicted_class_name.title(), third_predicted_class_name.title()]
