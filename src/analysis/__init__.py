"""Bibliometric, temporal, and text-analytics pipelines."""

from __future__ import annotations

from .citation_network import (
    build_citation_graph,
    build_reference_index,
    compute_network_metrics,
    detect_communities,
    resolve_citations,
)
from .subfield_classifier import classify_corpus, classify_paper
from .temporal_analysis import compute_temporal_metrics, estimate_growth_rate
from .text_processing import build_tfidf_matrix, remove_stopwords, tokenize
from .topic_modeling import fit_nmf_topics, get_document_topics

__all__ = [
    "build_citation_graph",
    "build_reference_index",
    "build_tfidf_matrix",
    "classify_corpus",
    "classify_paper",
    "compute_network_metrics",
    "compute_temporal_metrics",
    "detect_communities",
    "estimate_growth_rate",
    "fit_nmf_topics",
    "get_document_topics",
    "remove_stopwords",
    "resolve_citations",
    "tokenize",
]
