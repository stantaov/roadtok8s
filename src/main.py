from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return {"Hello": "World"}

@app.get("/api/v1/hello-word/")
def read_hello_word():
    return {"what": "road", "where": "k8s", "version": "v1"}


