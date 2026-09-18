from fastapi import FastAPI

from app.graph import graph
from app.models import AskRequest
from app.models import AskResponse

app = FastAPI()


@app.post(
    "/ask",
    response_model=AskResponse
)
def ask(request: AskRequest):

    result = graph.invoke({
        "query": request.query
    })

    return AskResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=1.0
    )