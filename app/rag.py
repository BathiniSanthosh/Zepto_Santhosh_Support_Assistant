from db import collection

CONFIDENCE_THRESHOLD = 0.4


def retrieve(question):

    try:

        results = collection.query(
            query_texts=[question],
            n_results=3
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        if not documents:

            return {
                "status": "no_match",
                "answer": "Sorry, I could not find any information related to your question in the Zepto knowledge base.",
                "sources": [],
                "confidence": 0.0
            }

        sources = [
            m.get("source", "unknown")
            for m in metadatas
        ]

        confidence = min(
            len(documents) * 0.3,
            0.9
        )

        if confidence < CONFIDENCE_THRESHOLD:

            return {
                "status": "low_confidence",
                "answer": "The question does not appear to be related to Zepto support documents.",
                "sources": [],
                "confidence": confidence
            }

        return {
            "status": "success",
            "answer": documents[0],
            "sources": sources,
            "confidence": confidence
        }

    except Exception as e:

        return {
            "status": "error",
            "answer": f"Error: {str(e)}",
            "sources": [],
            "confidence": 0.0
        }
