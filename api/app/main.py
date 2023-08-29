from fastapi import FastAPI


app = FastAPI()

@app.get("/versicle")
async def versicle():
    return {"versicle": "test"}

