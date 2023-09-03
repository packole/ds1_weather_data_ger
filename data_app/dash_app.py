# Basics
import pandas as pd
import numpy as np
# Data Visualization
import plotly.express as px
# Dash
import dash
# Layout
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# DataTable
import dash_table
# Callbacks
from dash.dependencies import Input, Output


# Global Data 
weather_data_path = /home/phillip/Dokumente/repositories/ds1_weather
stations_data_path = "/Dokumente/repositories/ds1_weather_data_ger/database/raw_data_stations/stations_basedata.txt"



df_ny = pd.read_csv("data\AB_NYC_2019.csv")
df_hotel_bookings = pd.read_csv("data\hotel_bookings.csv")