# Use a pipeline as a high-level helper
import os
from transformers import pipeline
from dotenv import load_dotenv
from openai import OpenAI

def object_detection(imgUrl):
    # Use a pipeline as a high-level helper
    object_detection_pipe = pipeline("object-detection", model="facebook/detr-resnet-50")
    # Pass the image URL and the text prompt to the model
    results = object_detection_pipe(imgUrl)
    labels = [item['label'] for item in results]

    return labels

def textGeneration(msg):
    client = OpenAI()
    msg_list = [{"role": "system", "content": "You are an advocate of sustainability. With the object given, come up with a creative way to reuse this object. "}]
    msg_list. append(msg)

    response = client.chat.completions.create(
        model= "gpt-4o-mini", #"gpt-4o"
        temperature=0.2,
        max_completion_tokens = 200, 
        messages = msg_list
    )
    out_message = response.choices[0].message.content
    return(out_message)

def firstObject():
    image_folder = 'static/imgs/shots'
    # List all image filenames in the folder
    images = os.listdir(image_folder)
    images.sort()
    scenario  = object_detection('static/imgs/shots/' + images[-1])
    unique_scenario_list = list(set(scenario))
    object_list = []
    for item in unique_scenario_list:
        if(item!="person"):
            object_list.append(item)
    if object_list.count > 0:
        return object_list[0]
    else:
        return "none"

def runModels():
    first_object = firstObject
    reuse_idea = "No object recognized"


    if first_object != "none":
        msg = {"role": "user", "content": first_object}
        reuse_idea = textGeneration(msg)


    return([first_object,reuse_idea])