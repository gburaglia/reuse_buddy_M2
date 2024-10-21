# Overview
Interactive Flask application with P5.js, a detection transformer (DETR) AI model for object detection from Hugging Face, and a language model from OpenAI. Created for the class LMC 8803 GM1 AI 4 DM taught by Brian Magerko and Manoj Deshpande at Georgia Tech.

# Motivation
To create an interface to help you think of ways to reuse common household objects. You first, take a picture of your object, if is displayed in the gallery for you to view, if you are not satisfied with the image you can continue taking pictures, once you are satisfied, the primary AI model will identify the object, and the secondary AI model comes up with a creative way to reuse the object detected.

# Technical Specifications: 
Flask application
Hugging Face object detection model: facebook/detr-resnet-50 
OpenAI model: gpt-4o

# Demo Video: 
[Demo Video](https://youtu.be/xU3obn9Bo_I)

# Demo Snapshot: 
![Demo Snapshot](/static/imgs/demo_snapshot.png)

# Instructions: 
Once your virtual environment is active: `pip install -r requirements.txt`
Create an ".env" file to store all the environment variables for Flask, Huggingface, OpenAI & Langchain. Copy this code into the ".env" file. And complete with your hugging face and openai keys.
    - `FLASK_APP = app`
    - `FLASK_RUN_PORT = 8080`
    - `FLASK_DEBUG = True`
    - `HF_TOKEN = ""`
    - `OPENAI_API_KEY = ""`