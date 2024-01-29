import streamlit as st

st.set_page_config(
    page_title="III OGA Chair Group - CHALLENGE",
    page_icon="../images/streamlit/oga_favicon.png",
    layout="wide",
)


from PIL import Image

from utils import load_css, load_theme
from utils.data import (
    houseshold_debt_all_countries,
    household_debt_all_instruments_all_countries,
    nonfinancial_corporate_debt_all_instruments,
    private_debt_all_countries,
    private_debt_all_instruments_all_countries,
    central_goverment_debt,
    general_goverment_debt,
    nonfinancial_public_sector_debt,
    public_sector_debt,
    global_heat
)
from views.parents import (
    AllDebtView,
    GlobalHeatView
)

load_css()
theme = load_theme()


class Menu:
    GROUP1 = "Global Private Debt"
    GROUP2 = "Global Public Debt"
    GROUP3 = "Global Heat"

    # GROUP1
    OPTION1 = "Private debt, loans and debt securities"
    OPTION2 = "Household debt, loans and debt securities"
    OPTION3 = "Nonfinancial corporate debt, loans and debt securities"
    OPTION4 = "Private debt, all instruments"
    OPTION5 = "Household debt, all instruments"
    # GROUP2
    OPTION6 = "Central Government Debt"
    OPTION7 = "General Government Debt"
    OPTION8 = "Nonfinancial Public Sector Debt"
    OPTION9 = "Public Sector Debt"
    # GROUP3
    OPTION10 = "Global Heat per Year"


with st.sidebar:

    menu_groups = [
        Menu.GROUP1, 
        Menu.GROUP2,
        Menu.GROUP3,    
    ]

    option_group_1 = [
        Menu.OPTION1, 
        Menu.OPTION2, 
        Menu.OPTION3,
        Menu.OPTION4,
        Menu.OPTION5,
    ]

    option_group_2 = [
        Menu.OPTION6,
        Menu.OPTION7, 
        Menu.OPTION8,
        Menu.OPTION9
    ]

    option_group_3 = [
        Menu.OPTION10
    ]

    # Menu bootstrap icon
    st.write('''
        <div class="fs-2 mb-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="currentColor" class="bi bi-justify" viewBox="1 1 16 16">
                <path fill-rule="evenodd" d="M2 12.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z">
                </path>
            </svg> 
            <text class="menu-text-representation">Menú</text>
        </div>
        ''', unsafe_allow_html=True)
    
    selection_dict = {
        Menu.GROUP1: option_group_1,
        Menu.GROUP2: option_group_2,
        Menu.GROUP3: option_group_3
    }

    selected_section = st.selectbox("Selecciona grupo: ", sorted(selection_dict.keys()))
    selected_page = st.radio("Selecciona subgrupo: ", sorted(selection_dict[selected_section]))

st.markdown("<h1 style='font-size: 350%'>Equipo 3. OGATHON</h1>", unsafe_allow_html=True)

with st.container():
    if selected_section == Menu.GROUP1:
        if selected_page == Menu.OPTION1:
            AllDebtView().view(
                Menu.OPTION1, 
                private_debt_all_countries, 
                theme=theme,
            )
        elif selected_page == Menu.OPTION2:
            AllDebtView().view(
                Menu.OPTION2, 
                houseshold_debt_all_countries, 
                theme=theme,
            )
        elif selected_page == Menu.OPTION3:
            AllDebtView().view(
                Menu.OPTION3,
                nonfinancial_corporate_debt_all_instruments,    
                theme=theme,
            )
        elif selected_page == Menu.OPTION4:
            AllDebtView().view(
                Menu.OPTION4,
                private_debt_all_instruments_all_countries,
                theme=theme,
            )
        elif selected_page == Menu.OPTION5:
            AllDebtView().view(
                Menu.OPTION5, 
                household_debt_all_instruments_all_countries, 
                theme=theme,
            )   
    elif selected_section == Menu.GROUP2:
        if selected_page == Menu.OPTION6:
            AllDebtView().view(
                Menu.OPTION6,
                central_goverment_debt,
                theme=theme,
            )
        elif selected_page == Menu.OPTION7:
            AllDebtView().view(
                Menu.OPTION7,
                general_goverment_debt,
                theme=theme,
            )
        elif selected_page == Menu.OPTION8:
            AllDebtView().view(
                Menu.OPTION8,
                nonfinancial_public_sector_debt,
                theme=theme,
            )
        elif selected_page == Menu.OPTION9:
            AllDebtView().view(
                Menu.OPTION9,
                public_sector_debt,
                theme=theme,
            )
    elif selected_section == Menu.GROUP3:
        if selected_page == Menu.OPTION10:
            GlobalHeatView().view(
                Menu.OPTION10,
                global_heat,
                theme=theme
            )

st.image(Image.open("../images/streamlit/oga_logo.png"), width=150)