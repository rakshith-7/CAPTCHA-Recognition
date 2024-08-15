# CAPTCHA-Recognition
Alphanumeric Captcha Recognition using CNN

This project is an Alphanumeric CAPTCHA Recognition tool using Convolutional Neural Networks (CNN). The aim is to develop a model that can recognize and interpret CAPTCHAs with high accuracy, even when faced with various distortions like blur, strikeouts, or slanted characters.


Features
Alphanumeric CAPTCHA Recognition: The model can recognize and interpret distorted alphanumeric CAPTCHA images.
Web Interface: A user-friendly interface is provided for uploading CAPTCHA images and getting the recognized text as output.
Model Training: The project includes a Jupyter notebook used for training the CNN model on the CAPTCHA dataset.
Getting Started
Prerequisites
Ensure you have the following installed on your system:

Python 3.x
Flask
Jupyter Notebook
TensorFlow/Keras
Bootstrap and Materialize CSS (for the frontend)

Install Dependencies - 

Install the required Python packages

Run the Backend Server - 

Navigate to the Backend/ directory and start the Flask server:

Access the Web Interface

Open homepage.html in your browser to interact with the CAPTCHA recognition tool.

Using the Tool

Upload a CAPTCHA image using the web interface.
The image will be processed by the backend, and the recognized text will be displayed on the UI.
Training the Model
If you want to retrain the model:

Open the Jupyter notebook located in Training-Files/



Note
The Data/ folder contains the main dataset with 1000 images.
The Validate/ folder contains 70 images used for validation.
The trained model is stored in Trained-Model/captca_rec_model.h5.



Authors
Rakshith V Patil 
