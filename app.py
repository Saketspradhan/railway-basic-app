from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.post("/display_text/")
async def display_text(text: str):
    return {"text": text}
