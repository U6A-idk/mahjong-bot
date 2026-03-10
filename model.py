import matplotlib.pyplot as plt
import numpy as np
import PIL

import pathlib
from pathlib import Path
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import os
import shutil

# Use the new LiteRT interpreter instead of deprecated tf.lite.Interpreter
from ai_edge_litert import interpreter as litert_interpreter

# Loading the model
TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

interpreter = litert_interpreter.Interpreter(model_path=TF_MODEL_FILE_PATH)
interpreter.allocate_tensors()

# Print the signatures from the converted model
signatures = interpreter.get_signature_list()
print("Signatures:", signatures)

# Test by passing the signature name if available
if 'serving_default' in signatures:
    classify_lite = interpreter.get_signature_runner('serving_default')
    print("Signature runner created")
else:
    print("No serving_default signature found")

# Model parameters
img_height = 320
img_width = 240
class_names = ['bamboo-1', 'bamboo-2', 'bamboo-3', 'bamboo-4', 'bamboo-5', 'bamboo-6', 'bamboo-7', 'bamboo-8', 'bamboo-9', 
               'bonus-autumn', 'bonus-bamboo', 'bonus-chrysanthemum', 'bonus-orchid', 'bonus-plum', 'bonus-spring', 'bonus-summer', 'bonus-winter', 
               'characters-1', 'characters-2', 'characters-3', 'characters-4', 'characters-5', 'characters-6', 'characters-7', 'characters-8', 'characters-9', 
               'dots-1', 'dots-2', 'dots-3', 'dots-4', 'dots-5', 'dots-6', 'dots-7', 'dots-8', 'dots-9', 
               'honors-east', 'honors-green', 'honors-north', 'honors-red', 'honors-south', 'honors-west', 'honors-white']

# Trying it out on new data
test_path = Path("C:/Users/deanl/Desktop/mahjong-bot/mahjong-dataset-master/train/test/test7tong.jpg")

if test_path.exists():
    img = tf.keras.utils.load_img(
        test_path, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    # Use the signature runner for prediction
    predictions = classify_lite(keras_tensor_15=img_array)
    score = tf.nn.softmax(predictions['output_0'][0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
else:
    print(f"Test image not found at {test_path}")