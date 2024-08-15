import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
import time
import json
import cv2
import os
from PIL import Image
import sys
import warnings
warnings.filterwarnings("ignore")
import requests
from flask_cors import CORS, cross_origin
import pathlib

from keras import layers
from keras.models import Model
from keras.models import load_model
from keras import callbacks
import string

from keras.models import load_model
model = load_model('../Trained Model/captca_rec_model.h5')
if model:
    print("model loaded")

#Init main values
symbols = string.ascii_lowercase + "0123456789" # All symbols captcha can contain
num_symbols = len(symbols)
img_shape = (50, 200, 1)

app = Flask(__name__)
#api = Api(app)
cors = CORS(app)
#, resources={r"/api/*": {"origins": "*"}}



######################################################################################################

# Function that fetches the image and predicts the output
def predict_(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = img / 255.0
    else:
        print("Not detected");
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
    return capt

######################################################################################################

#Route function 
@app.route('/captcha_image', methods=['GET', 'POST'])
@cross_origin()
def captcha_image():
    posteddata = request.get_json()

    try:
        img_path = "image.jpeg"
        pred_captcha = predict_(img_path)
        ret_msg = {"predicted_output": pred_captcha, "status": 200}
    except:
        ret_msg = {"status": 400}

    final_return_message = ret_msg

    return jsonify(final_return_message)



######################################################################################################

#Image Upload Route Function
@app.route('/fileupload',methods=['POST'])
@cross_origin()
def fileupload():
    #print("api called")
    current_directory = pathlib.Path(__file__).parent.absolute()
    file = request.files['image']
    file.save(os.path.join(current_directory,"image.jpeg"))
    return 'file saved'   


######################################################################################################

# API routing

if __name__ == "__main__":
    app.run(host="127.0.0.1")
    #port=80
