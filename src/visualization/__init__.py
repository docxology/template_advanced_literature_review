"""Publication-ready visualization generation."""

from __future__ import annotations

from .advanced_plots import (
    plot_cooccurrence_matrix,
    plot_dendrogram,
    plot_pca_embeddings,
    plot_term_heatmap,
    plot_topic_term_bars,
    plot_word_cloud,
)
from .citation_plots import plot_citation_network, plot_degree_distribution
from .field_overview import plot_field_summary, plot_subfield_distribution
from .hypothesis_charts import (
    plot_assertion_summary,
    plot_assertion_type_breakdown,
    plot_evidence_timeline,
    plot_hypothesis_dashboard,
)
from .style import VIZ_CONFIG
from .temporal_plots import plot_growth_curve, plot_subfield_timeline

__all__ = [
    "VIZ_CONFIG",
    "plot_assertion_summary",
    "plot_assertion_type_breakdown",
    "plot_citation_network",
    "plot_cooccurrence_matrix",
    "plot_degree_distribution",
    "plot_dendrogram",
    "plot_evidence_timeline",
    "plot_field_summary",
    "plot_growth_curve",
    "plot_hypothesis_dashboard",
    "plot_pca_embeddings",
    "plot_subfield_distribution",
    "plot_subfield_timeline",
    "plot_term_heatmap",
    "plot_topic_term_bars",
    "plot_word_cloud",
]
