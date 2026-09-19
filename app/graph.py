import logging

from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from rag import retrieve

logger = logging.getLogger(__name__)

logger.info("Loading graph.py")


class GraphState(TypedDict):

    question: str
    answer: str
    sources: list
    confidence: float


def agent(state):

    logger.info(
        f"Question: {state['question']}"
    )

    result = retrieve(
        state["question"]
    )

    answer = "\n".join(
        result["documents"]
    )

    return {

        "question": state["question"],

        "answer": answer,

        "sources": result["sources"],

        "confidence": result["confidence"]
    }


builder = StateGraph(
    GraphState
)

builder.add_node(
    "agent",
    agent
)

builder.set_entry_point(
    "agent"
)

builder.add_edge(
    "agent",
    END
)

graph = builder.compile()

logger.info(
    "Graph compiled successfully"
)
