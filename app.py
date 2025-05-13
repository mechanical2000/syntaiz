from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Syntaiz IA V1 API is running!"}
