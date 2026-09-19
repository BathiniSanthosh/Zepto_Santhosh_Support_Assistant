from pydantic import BaseModel
from typing import List
import logging

logger = logging.getLogger(__name__)
logger.info("models.py loaded")


class QueryRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float
