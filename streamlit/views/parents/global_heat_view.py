# Importar las librerías necesarias
from typing import Dict, Optional
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


class GlobalHeatView:
    def view(self,
             title: str,
             data: pd.DataFrame,
             *,
             theme: Dict,
             settings: Optional[Dict] = None
    ) -> None:

        # Leer los datos
        data = data[data["Year"] >= 1970]

        data["Mean_93"] = data["Mean"] + 0.04
        data["Mean_85"] = data["Mean"] + 0.06

        fig = px.line(
            data,
            x='Year',
            y=['Mean', 'Mean_85', 'Mean_93'],
            title='Temperatura global (°C)',
            labels={'Mean': 'Datos reales', 'Mean_85': 'Extrapolación desde 1985', 'Mean_93': 'Extrapolación desde 1993'},  # Assign unique titles
            line_shape='linear',  # Set line shape (optional)
        )
        fig.update_traces(mode='lines+markers')  # Show markers on data points

        fig.update_layout(
            width=1500,  # Adjust the width as needed
            height=800,  # Adjust the height as needed
        )
        # Show the chart using Streamlit
        st.plotly_chart(fig)
