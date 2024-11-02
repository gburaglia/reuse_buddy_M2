from langchain_openai import ChatOpenAI
from transformers import pipeline
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings #for converting chunks into embeddings
from langchain_chroma import Chroma #database for stroring the embeddings
import os

def firstObject():
    image_folder = 'static/imgs/shots'
    # List all image filenames in the folder
    images = os.listdir(image_folder)
    images.sort()
    if(images):
        scenario  = object_detection('static/imgs/shots/' + images[-1])
        unique_scenario_list = list(set(scenario))
        object_list = []
        for item in unique_scenario_list:
            if(item!="person"):
                object_list.append(item)
        if (object_list):
            return object_list[0]
        else:
            return "none"
    else:
        return "no image"

def object_detection(imgUrl):
    # Use a pipeline as a high-level helper
    object_detection_pipe = pipeline("object-detection", model="facebook/detr-resnet-50")
    # Pass the image URL and the text prompt to the model
    results = object_detection_pipe(imgUrl)
    labels = [item['label'] for item in results]

    return labels

def societal_definition(type):
    society_dict = {
        "Growing": "Focused on expansion, development, and continued acceleration.",
        "Collapsing": "Focused on the decline or breakdown of society, leading to a simpler society.",
        "Controlling": "Focused on managing and controlling societal excesses to preserve resources and maintain order, guided by various values and authoritarian control.",
        "Transforming": "Focused on embracing radical changes that reshapes humanity and the environment, leading to a posthuman future."
    }
    return society_dict.get(type,"")

def getRetriever(dir):
    """
    dir is the directory of the vector DB
    """
    embeddings_used = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorDB = Chroma(persist_directory=dir,embedding_function=embeddings_used)
    retriever = vectorDB.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return retriever

def textGeneration_langChain(msg,type):
    """
    msg is the object detected for the object reuse idea (hugging face model output);
    type is the sustainability suggestion mode - Growing, Collapsing, Controlling, Transforming
    """
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.2,
        max_tokens=200,
        timeout=None,
        max_retries=2
    )

    defintion = societal_definition(type)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an advocate of sustainability. With the object given, come up with a way to reuse this object in the future. From the viewpoint of a society that is {suggestion_mode}. A {suggestion_mode} society is defined as one that is: {societal_definition}."
            ),
            (
                "human", 
                "{scenario_lang}"
            ),
        ]
    )

    chain = prompt | llm | StrOutputParser()

    out_message = chain.invoke({
        "suggestion_mode" : type,
        "scenario_lang" : msg,
        "societal_definition": defintion,
    })

    return out_message

def textGeneration_langChain_RAG(msg,type, retrieverDir):
    """
    msg is the object detected for the object reuse idea (hugging face model output);
    type is the sustainability suggestion mode - Growing, Collapsing, Controlling, Transforming
    """
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.2,
        max_tokens=200,
        timeout=None,
        max_retries=2
    )

    defintion = societal_definition(type)

    system_prompt = (
        "You are an advocate of sustainability. With the object given, come up with a way to reuse this object in the future. From the viewpoint of a society that is {suggestion_mode}. A {suggestion_mode} society is defined as one that is: {societal_definition}."
        "Use the following pieces of retrieved context to generate sustainable, upcycled, object reuse ideas. "
        "Keep the idea to less than 100 words."
        "\n\n"
        "{context}"
    )


    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system", 
                system_prompt
            ),
            (
                "human", 
                "{scenario_lang}"
            ),
        ]
    )

    rag_chain = prompt | llm | StrOutputParser()

    retriever = getRetriever(retrieverDir)

    out_message = rag_chain.invoke({
            "context":retriever,
            "suggestion_mode" : type,
            "scenario_lang" : msg,
            "societal_definition": defintion,
        })

    return out_message

def runModels2(type):
    first_object = firstObject()
    reuse_idea = ""
    if first_object == "none":
        reuse_idea = "Error: No object recognized"
    elif first_object == "no image":
        reuse_idea = "Error: No image submitted, take a picture first!"
    else:
        cwd = os.getcwd()
        db_dir = os.path.join(cwd,"chroma_db")
        reuse_idea = textGeneration_langChain_RAG(first_object,type,db_dir)


    return([first_object,reuse_idea])