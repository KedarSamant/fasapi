from fastapi import FastAPI# This imports the main FastAPI class that we need to create our application.

app=FastAPI()#We create an instance of FastAPI. This app variable will be the main point of interaction with our API.

@app.get('/')#This is a decorator that tells FastAPI that the function right below it corresponds to:
# A request to the path / (the root URL)
# Using a GET operation (when someone visits the URL in a browser)
def read_root():
    return {'message':'hello world'}# FastAPI automatically converts this dict to JSON format.


