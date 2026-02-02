import os
import uvicorn
import multiprocessing

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from src.base.llm_model import get_hf_llm, get_llama_llm
from src.rag.main import build_rag_chain, InputQA, OutputQA


PATH_MODEL = os.environ.get("PATH_MODEL")
GENAI_DOCS = os.environ.get("PATH_TO_DOCS")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="My first simple API server using LangChain"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

genai_chain = None

def init_rag_chain():
    # llm = get_hf_llm(temperature=0.5)
    llm = get_llama_llm(model_file=PATH_MODEL)

    return build_rag_chain(
        llm,
        data_dir=GENAI_DOCS,
        data_type="pdf"
    )


# --------- Routes ----------
@app.get("/check")
async def check():
    return {"status": "OK"}

@app.post("/generative_ai", response_model=OutputQA)
async def generative_ai(input: InputQA):
    answer = genai_chain.invoke(input.question)
    return {"answer": answer}


if __name__ == "__main__":
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn", force=True)

    genai_chain = init_rag_chain()

    # LangServe routes (add only after chain ready)
    add_routes(
        app,
        genai_chain,
        playground_type="default",
        path="/generative_ai"
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)
