import os
os.environ["TOKENIZERS_PARALLELISH"] = "false"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langserve import add_routes

from src.base.llm_model import get_hf_llm, get_llama_llm
from src.rag.main import build_rag_chain, InputQA, OutputQA

# llm = get_hf_llm(temperature = 0.5)
llm = get_llama_llm(model_file="./src/base/llama-2-7b-chat.Q6_K.gguf")
genai_docs = "./data_source/generative_ai"

genai_chain = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf") # create chains

# ------------- Create app FastAPI ---------------

app = FastAPI(
    title= "LangChain Server", 
    version = "1.0",
    description = "My first simple API server using LangChain"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# ------------- Add routes to app ---------------
@app.get("/check")
async def check():
    return {"status": "OK"}

@app.post("/generative_ai", response_model=OutputQA)
async def generative_ao(input: InputQA):
    answer = genai_chain.invoke(input.question)
    return {"answer": answer}

add_routes(app, genai_chain, playground_type="default", path="/generative_ai") # langserve
