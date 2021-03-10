import numpy as np
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model
from keras.preprocessing import image

''' 
Create and use keras VGG16 pretrained model to extract features from an image
Author: Weronika Wolska
Created: 06.03.2021
'''


class FeatureExtractor:

    def __init__(self):
        model = VGG16(weights='imagenet', include_top=True)
        # specify fc7 as the output layer
        self.output_model = Model(inputs=model.input, outputs=model.get_layer('fc2').output)

    @staticmethod
    def load_image(image_path):
        load_image = image.load_img(image_path, target_size=(224, 224))
        return load_image

    def extract_features(self, image_path):
        """
        :param image_path: path to the image
        :return: vector with features'/media/taika/Data1/Pictures/coil-100'
        """
        img = self.load_image(image_path)
        img_features = image.img_to_array(img)
        img_features = np.expand_dims(img_features, axis=0)
        img_features = preprocess_input(img_features)

        feature = self.output_model.predict(img_features)
        # flatten tensor to vector
        return np.array(feature).flatten()

