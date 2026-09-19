from fastapi import FastAPI

from models import (
    QueryRequest,
    AnswerResponse
)

from graph import graph
from ingest import ingest_documents, collection

app = FastAPI(
    title="Zepto Support Assistant"
)


@app.on_event("startup")
def startup_event():

    if collection.count() == 0:
        ingest_documents()


@app.get("/")
def root():
    return {"status": "running"}


@app.post(
    "/ask",
    response_model=AnswerResponse
)
def ask(request: QueryRequest):

    result = graph.invoke({
        "question": request.question
    })

    return AnswerResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"]
    )
