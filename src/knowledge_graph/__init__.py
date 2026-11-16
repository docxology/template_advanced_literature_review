"""Knowledge graph and nanopublication ontology."""

from __future__ import annotations

from .extraction import extract_assertions
from .graph_builder import KnowledgeGraph
from .hypothesis import Hypothesis, score_hypothesis
from .llm_extraction import LLMConfig, extract_assertions_llm
from .nanopublication import Assertion, Nanopublication
from .query import (
    count_triples_by_type,
    query_assertions_for_paper,
    query_contradicting_papers,
    query_papers_by_hypothesis,
    query_supporting_papers,
)
from .schema import AIF_NAMESPACE

__all__ = [
    "AIF_NAMESPACE",
    "Assertion",
    "Hypothesis",
    "KnowledgeGraph",
    "LLMConfig",
    "Nanopublication",
    "count_triples_by_type",
    "extract_assertions",
    "extract_assertions_llm",
    "query_assertions_for_paper",
    "query_contradicting_papers",
    "query_papers_by_hypothesis",
    "query_supporting_papers",
    "score_hypothesis",
]
