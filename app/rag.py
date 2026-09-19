import logging

from db import collection

logger = logging.getLogger(__name__)

logger.info("Loading rag.py")

# Questions outside Zepto domain
BLOCKED_TOPICS = [
    "python",
    "java",
    "cricket",
    "football",
    "movie",
    "netflix",
    "weather",
    "ai"
]


def retrieve(question: str):

    try:

        question_lower = question.lower()

        # Generic question detection
        if any(
            topic in question_lower
            for topic in BLOCKED_TOPICS
        ):

            return {
                "answer": (
                    "I am a Zepto Support Assistant. "
                    "Please ask questions related to Zepto services, "
                    "orders, refunds, deliveries, subscriptions "
                    "or payments."
                ),
                "sources": [],
                "confidence": 0.0
            }

        results = collection.query(
            query_texts=[question],
            n_results=3
        )

        documents = results.get(
            "documents",
            [[]]
        )[0]

        metadatas = results.get(
            "metadatas",
            [[]]
        )[0]

        if not documents:

            return {
                "answer": (
                    "Sorry, I could not find any relevant "
                    "information in the knowledge base."
                ),
                "sources": [],
                "confidence": 0.0
            }

        sources = []

        for meta in metadatas:

            if meta:
                sources.append(
                    meta.get(
                        "source",
                        "unknown"
                    )
                )

        return {
            "answer": documents[0],
            "sources": sources,
            "confidence": 0.90
        }

    except Exception as e:

        logger.exception(
            f"Retrieval failed: {e}"
        )

        return {
            "answer": "An unexpected error occurred.",
            "sources": [],
            "confidence": 0.0
        }
