from typing import Dict, Optional
import numpy as np
from plotly.graph_objects import Figure
import pandas as pd   
    

def add_quartiles(fig: Figure, data: pd.Series) -> Figure:
    fig.add_hline(
        y=data.quantile(0.5),
        line_dash="dash",
        line_color="black",
        annotation_text="<b>Mediana</b>          ",
        annotation_font_size=14,
    )
    fig.add_hrect(
        data.quantile(0.25),
        data.quantile(0.75),
        annotation_text="<b>IQR</b>",
        annotation_position="outside top right",
        annotation_font_size=14,
        fillcolor="#0180c6",
        opacity=0.25,
        line_width=0,
    )

    return fig

def add_mean_with_quartiles(fig: Figure, data: pd.Series) -> Figure:
    fig.add_hline(
        y=data.mean(),
        line_dash="dash",
        line_color="black",
        annotation_text="<b>Media</b>          ",
        annotation_font_size=14,
    )

    return fig


def style_bar_plot(
    fig: Figure, theme: Dict, settings: Optional[Dict] = None, grouping_customdata=None
) -> Figure:
    if grouping_customdata:
        groups = np.unique(fig["data"][0]["customdata"][:, grouping_customdata])

        style_elements = [(p,c) for p in PATTERNS for c in COLORS]

        style_map = dict(zip(groups, style_elements))
        bar_colors = [
            style_map[g][1] for g in fig["data"][0]["customdata"][:, grouping_customdata]
        ]
        bar_patterns = [
            style_map[g][0] for g in fig["data"][0]["customdata"][:, grouping_customdata]
        ]

        fig.update_traces(
            marker_color=bar_colors,
            marker_pattern_shape=bar_patterns,
            marker_line_width=0,
        )

    else:
        fig.update_traces(
            marker_color=theme["primaryColor"],
            marker_line_width=0,
        )
    fig.update_xaxes(
        tickangle=-55,
        showline=True,
        linewidth=2,
        linecolor=theme["secondaryColor"],
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=theme["secondaryColor"],
    )

    return fig


def style_line_plot(fig: Figure, theme: Dict) -> Figure:
    fig.update_traces(
        line_color=theme["primaryColor"],
        line_width=3,
        marker_color=theme["primaryColor"],
        marker_line_width=0,
    )
    fig.update_xaxes(
        tickangle=-55,
        showline=True,
        linewidth=2,
        linecolor=theme["secondaryColor"],
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=theme["secondaryColor"],
    )

    return fig


def style_pie_plot(fig: Figure, theme: Dict) -> Figure:
    fig.update_traces(
        marker_colors=COLORS_RED,
    )

    return fig


COLORS = [
    "#e51b20",
    "#ac344a",
    "#734e73",
    "#3a679d",
    "#0180c6",
]

COLORS_RED = [
    "#7e0e11",
    "#b21418",
    "#e51b20",
    "#ea462d",
    "#ee623d",
    "#f2794f",
    "#f68f63",
    "#f9a378",
    "#fbb790",
    "#fdcaa9",
    "#ffdcc4",
    "#ffeadb",
]

PATTERNS = [
    '',
    'x',
]

LINES = ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]
