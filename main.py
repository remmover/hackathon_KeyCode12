from fastapi import FastAPI, requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "APP"}


@app.post("/")
def write_root(requests):
    return requests
