from inference_sdk import InferenceHTTPClient
import os

import matplotlib.pyplot as plt
import numpy as np
import PIL

import pathlib
from pathlib import Path
import pandas as pd

import base64

import json

import cv2

import math

image_url = "C:/Users/deanl/Desktop/mahjong-bot/mahjong-dataset-master/train/test/testfullset.jpg"

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="dtETuhTjbIw3z9gJenuJ"
)

predictions = CLIENT.infer([image_url], model_id="master-oez61/7")

image_mat = cv2.imread(image_url)

for bounding_box in predictions['predictions']:
    x0 = bounding_box['x'] - bounding_box['width'] / 2
    x1 = bounding_box['x'] + bounding_box['width'] / 2
    y0 = bounding_box['y'] - bounding_box['height'] / 2
    y1 = bounding_box['y'] + bounding_box['height'] / 2
    
    start_point = (int(x0), int(y0))
    end_point = (int(x1), int(y1))
    cv2.rectangle(image_mat, start_point, end_point, color=(0,0,0), thickness=2)
    
    cv2.putText(
        image_mat,
        bounding_box["class"],
        (int(x0), int(y0) - 10),
        fontFace = cv2.FONT_HERSHEY_SIMPLEX,
        fontScale = 0.6,
        color = (0, 0, 0),
        thickness=2
    )

    cv2.putText(
        image_mat,
        str((round(bounding_box["confidence"], 2))*100) + "%",
        (int(x0) + 40, int(y0) - 10),
        fontFace = cv2.FONT_HERSHEY_SIMPLEX,
        fontScale = 0.6,
        color = (0, 0, 0),
        thickness=2
    )
    
cv2.imwrite("example_with_bounding_boxes.jpg", image_mat)