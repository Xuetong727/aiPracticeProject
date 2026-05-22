from fastapi import FastAPI,HTTPException # type: ignore
from service import llm_service

app = FastAPI()



@app.get("/")
async def root():
    return {"message":"This is a ai practice project"}

@app.get("/chat")
async def chat(query:str):
    return llm_service.call_llm(query)
