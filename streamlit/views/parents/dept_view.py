from typing import Dict, Optional

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


class AllDebtView:
    def view(self,
             title: str,
             data: pd.DataFrame,
             *,
             theme: Dict,
             settings: Optional[Dict] = None
    ) -> None:
        st.cache_data()
        st.title(title)

        years = []
        # Selectbox for choosing the year value
        for col in data.columns:
            if len(str(col)) <= 4:
                years.append(col)
            else:
                data = data.rename(columns={col: 'Country'})
        selected_year = st.selectbox("Select the year to visualize:", years)
        
        plot_data = data.copy()
        plot_data[selected_year] = plot_data[selected_year].apply(lambda x: -1 if x == 'no data' else x)
        plot_data = plot_data.sort_values(by=selected_year).reset_index(drop=True)
        
        st.info('Data with value -1 mean "no data"')
        # Create a choropleth map using Plotly Express
        fig1 = px.choropleth(
            plot_data[['Country', selected_year]],
            locations='Country',
            locationmode='country names',
            color=selected_year,
            projection='natural earth',
            color_continuous_scale='Bluyl',
            title=f'World Map - {title}',
        )

        # Update the layout to change the size of the map
        fig1.update_layout(
            geo=dict(
                showframe=False,
                # showcoastlines=False,
                projection_type='natural earth'
            ),
            height=800,  # Adjust the height as needed
            width=1500,   # Adjust the width as needed
        )

        # Show the map using Streamlit
        st.plotly_chart(fig1)

        trend_values = []
        for year in years:
            val = data[data[year] != 'no data'][year].mean()
            trend_values.append(val)

        trend_data = {
            'Date': years,
            'Value': trend_values
        }

        fig2 = px.line(trend_data, x='Date', y='Value', title='Trend Line Plot')
        fig2.update_traces(mode='lines+markers')  # Show markers on data points

        fig2.update_layout(
            width=1500,  # Adjust the width as needed
            height=800,  # Adjust the height as needed
        )
        # Show the chart using Streamlit
        st.plotly_chart(fig2)

