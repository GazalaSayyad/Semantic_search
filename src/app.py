import uvicorn
from fastapi import FastAPI
from typing import List,Set, Optional
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import torch
from main import SemanticSearch

app = FastAPI(
    title="Semantic Search API",
    description="A simple Search Engine API that use NLP model to understand query",
    version="0.1",
)

class Recommend(BaseModel):
    queries: List[str] = []


@app.post("/search")
async def predict_sem(query: Recommend):
    Sem_search=SemanticSearch()
    Sem_search.train_model()
    val=Sem_search.predict_sem(query.queries)
    return val

    