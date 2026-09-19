import logging

from db import collection

logger = logging.getLogger(__name__)

logger.info("Loading rag.py")


def retrieve(question):

    try:

        if collection is None:

            return {
                "documents": [],
                "sources": [],
                "confidence": 0.0
            }

        results = collection.query(
            query_texts=[question],
            n_results=3
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        sources = []

        for meta in metadatas:

            sources.append(
                meta.get("source", "unknown")
            )

        confidence = min(
            len(documents) * 0.3,
            0.95
        )

        return {
            "documents": documents,
            "sources": sources,
            "confidence": confidence
        }

    except Exception as e:

        logger.exception(
            f"Retrieval failed: {e}"
        )

        return {
            "documents": [],
            "sources": [],
            "confidence": 0.0
        }
