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

# Directory for the datasets
dataset_url_csv = Path("C:/Users/deanl/Desktop/mahjong-bot/mahjong-dataset-master/train/data.csv")
dataset_url_images = Path("C:/Users/deanl/Desktop/mahjong-bot/mahjong-dataset-master/train/images")

# Using pandas
df = pd.read_csv(dataset_url_csv)

import os
import shutil

# Create subdirectories for each unique label
unique_labels = df['label-name'].unique()
for label in unique_labels:
    label_dir = dataset_url_images / label
    label_dir.mkdir(exist_ok=True)

# Move images to their respective label directories
for _, row in df.iterrows():
    image_name = row['image-name']
    label_name = row['label-name']
    src_path = dataset_url_images / image_name
    dst_path = dataset_url_images / label_name / image_name
    if src_path.exists():
        shutil.move(str(src_path), str(dst_path))

# Check image count in the dataset
# image_count = len(list(dataset_url_images.glob('*.jpg')))
# print(image_count)

# Define parameters for the loader
batch_size = 32
img_height = 180
img_width = 180

# Validation split
train_dataset = tf.keras.utils.image_dataset_from_directory(
  dataset_url_images,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

validate_dataset = tf.keras.utils.image_dataset_from_directory(
  dataset_url_images,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# Print all the tile names in the dataset
class_names = train_dataset.class_names
print(class_names)

# Visualising data
plt.figure(figsize=(10, 10))
for images, labels in train_dataset.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

# Configure the dataset for performance
AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validate_dataset = validate_dataset.cache().prefetch(buffer_size=AUTOTUNE)

# Standardize the data
normalization_layer = layers.Rescaling(1./255)

# Apply normalization to the datasets
normalized_train_ds = train_dataset.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_train_ds))
first_image = image_batch[0]



