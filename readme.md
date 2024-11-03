# Overview
Interactive Flask application with P5.js, a detection transformer (DETR) AI model for object detection from Hugging Face, and a language model from OpenAI leveraging prompt templates and RAG capabilities using LangChain for further customization. Created for the class LMC 8803 GM1 AI 4 DM taught by Brian Magerko and Manoj Deshpande at Georgia Tech.

# Motivation
To create an interface to help you think of ways to reuse common household objects. You first, take a picture of your object, if is displayed in the gallery for you to view, if you are not satisfied with the image you can continue taking pictures, once you are satisfied, the primary AI model will identify the object, and the secondary AI model comes up with a creative way to reuse the object detected using prompt templates and RAG capabilities.

# Technical Specifications: 
Flask application
Hugging Face object detection model: facebook/detr-resnet-50 
OpenAI model: gpt-4o
Prompt templates: incorproate a selection of a [future type](https://www.iese.edu/insight/articles/future-scenarios-imagine/)
RAG datasource: pdf with [creative reuse examples](https://malmostudenter.se/wp-content/uploads/Upcycling-guide.pdf)

# Demo Video: 
[Demo Video](https://youtu.be/xxYSSstySh8)

# Demo Snapshot: 
![Demo Snapshot](/static/imgs/demo_snapshot_2.png)

# Instructions: 
Once your virtual environment is active: `pip install -r requirements.txt`
Create an ".env" file to store all the environment variables for Flask, Huggingface, OpenAI & Langchain. Copy this code into the ".env" file. And complete with your hugging face and openai keys.
    - `FLASK_APP = app`
    - `FLASK_RUN_PORT = 8080`
    - `FLASK_DEBUG = True`
    - `HF_TOKEN = ""`
    - `OPENAI_API_KEY = ""`