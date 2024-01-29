import pandas as pd
import xlrd
import numpy as np
import pathlib
import streamlit as st


@st.experimental_memo
def load_data(filename: str) -> pd.DataFrame:
    """Funtion to load diffetenc data format

    Args:
        filename (str): name of the file to load with type

    Returns:
        pd.DataFrame: read file as pandas DataFrame
    """
    filename = pathlib.Path(filename)
    if filename.suffix == ".html":
        data = pd.read_html(filename)[0]
    elif filename.suffix == ".csv":
        try:
            data = pd.read_csv(filename, low_memory=False)
        except:
            data = pd.read_csv(filename, sep=';', decimal=',', encoding='latin1')
    elif filename.suffix == ".parquet":
        data = pd.read_parquet(filename)
    elif filename.suffix == ".xlsx":
        data = pd.read_excel(filename)
    elif filename.suffix == ".xls":
        workbook = xlrd.open_workbook(filename, ignore_workbook_corruption=True)
        data = pd.read_excel(workbook)

    return data


# Main data paths
private_debt_data_path = '../data/input_data/global_debt_database/private_debt/'
public_debt_data_path = '../data/input_data/global_debt_database/public_debt/'
global_heat_data_path = '../data/input_data/globalheat/'

# Reading data
houseshold_debt_all_countries = load_data(private_debt_data_path + 'household_debt_all_countries.xls').dropna()
household_debt_all_instruments_all_countries = load_data(private_debt_data_path + 'household_debt_all_instruments_all_countries.xls').dropna()
nonfinancial_corporate_debt_all_instruments = load_data(private_debt_data_path + 'nonfinancial_corporate_debt_all_instruments.xls').dropna()
private_debt_all_countries = load_data(private_debt_data_path + 'private_debt_all_countries.xls').dropna()
private_debt_all_instruments_all_countries = load_data(private_debt_data_path + 'private_debt_all_instruments_all_countries.xls').dropna()

central_goverment_debt = load_data(public_debt_data_path + 'central_goverment_debt.xls').dropna()
general_goverment_debt = load_data(public_debt_data_path + 'general_goverment_debt.xls').dropna()
nonfinancial_public_sector_debt = load_data(public_debt_data_path + 'nonfinancial_public_sector_debt.xls').dropna()
public_sector_debt = load_data(public_debt_data_path + 'public_sector_debt.xls').dropna()

global_heat = load_data(global_heat_data_path + "annual.csv")


