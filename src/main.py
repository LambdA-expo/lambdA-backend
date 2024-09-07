from fastapi import FastAPI , Response

app = FastAPI()

@app.get("/")
async def home(response: Response):
    return {"message": "Welcome to Lambda!!"}