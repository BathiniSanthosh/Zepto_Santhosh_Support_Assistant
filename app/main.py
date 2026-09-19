import logging
import time
from typing import Dict, List

from ingest import collection

# ------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("rag.py loaded successfully")


# ------------------------------------------------------------------
# Retrieve Documents
# ------------------------------------------------------------------

def retrieve(question: str) -> Dict:

    start_time = time.time()

    logger.info("=" * 60)
    logger.info(f"RETRIEVE STARTED")
    logger.info(f"Question: {question}")

    try:

        doc_count = collection.count()

        logger.info(
            f"Collection contains {doc_count} documents"
        )

        if doc_count == 0:

            logger.warning(
                "Collection is empty"
            )

            return {
                "documents": [],
                "sources": [],
                "confidence": 0.0
            }

        logger.info(
            "Running Chroma query..."
        )

        results = collection.query(
            query_texts=[question],
            n_results=3
        )

        logger.info(
            "Chroma query completed successfully"
        )

        documents = results.get(
            "documents",
            [[]]
        )[0]

        metadatas = results.get(
            "metadatas",
            [[]]
        )[0]

        logger.info(
            f"Retrieved {len(documents)} documents"
        )

        sources = []

        for metadata in metadatas:

            if metadata:

                sources.append(
                    metadata.get(
                        "source",
                        "unknown"
                    )
                )

        confidence = round(
            min(
                len(documents) * 0.30,
                0.95
            ),
            2
        )

        elapsed = round(
            time.time() - start_time,
            2
        )

        logger.info(
            f"Retrieval completed in {elapsed}s"
        )

        logger.info(
            f"Sources: {sources}"
        )

        logger.info(
            f"Confidence: {confidence}"
        )

        return {
            "documents": documents,
            "sources": sources,
            "confidence": confidence
        }

    except Exception as e:

        logger.exception(
            f"Retrieval error: {str(e)}"
        )

        return {
            "documents": [],
            "sources": [],
            "confidence": 0.0
        }

    finally:

        logger.info(
            "RETRIEVE FINISHED"
        )

        logger.info("=" * 60)
