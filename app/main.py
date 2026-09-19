from fastapi import FastAPI
from models import QueryRequest, AnswerResponse
from graph import graph
from ingest import ingest_documents, collection

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("main.py loaded")

app = FastAPI(
    title="Zepto Support Assistant"
)


@app.on_event("startup")
def startup_event():

    logger.info("Application startup")

    try:

        count = collection.count()

        logger.info(
            f"Collection count = {count}"
        )

        if count == 0:

            logger.info(
                "Starting ingestion..."
            )

            ingest_documents()

    except Exception as e:

        logger.exception(
            f"Startup failed: {e}"
        )


@app.get("/")
def root():

    logger.info("Health endpoint called")

    return {
        "status": "running"
    }


@app.post(
    "/ask",
    response_model=AnswerResponse
)
def ask(request: QueryRequest):

    logger.info(
        f"Question received: {request.question}"
    )

    try:

        result = graph.invoke(
            {
                "question": request.question
            }
        )

        logger.info(
            "Graph execution complete"
        )

        return AnswerResponse(
            answer=result["answer"],
            sources=result["sources"],
            confidence=result["confidence"]
        )

    except Exception as e:

        logger.exception(
            f"Ask endpoint failed: {e}"
        )

        raise
