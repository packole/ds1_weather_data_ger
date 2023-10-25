from dash import Dash, html, dcc
import os
import pandas as pd
import plotly.express as px

#define data sources path
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
stations_data_file = "station_data_transformed.csv"
weather_data_file = "weather_data_transformed.csv"

weather_data_path = os.path.join(data_dir, weather_data_file )
stations_data_path= os.path.join(data_dir, stations_data_file)

#read in data
weather_data = pd.read_csv(weather_data_path)
stations_data = pd.read_csv(stations_data_path)

#create instance
app = Dash(__name__)

#define map as a figure
map_fig = px.scatter_mapbox(
            stations_data,  # Ihr DataFrame
            lat='geo_width',  # Spalte für die Breite
            lon='geo_length',  # Spalte für die Länge
            hover_name='city',
            hover_data=["station_id","date_commissioning","heigth_station[m]","geo_width","geo_length"],
            color_discrete_sequence=["fuchsia"], 
            zoom=3, 
            height=300)


map_fig.update_layout(mapbox_style="open-street-map")
map_fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


#create layout of the app
app.layout = html.Div([
    html.H1("Weather Data Germany - Data Analytics Example"),
    html.P('I decided to built a data app for the weather data of different cities in Germany. In the following map you can see the choosed cities:'),
    dcc.Graph(
        id='map',
        figure=map_fig
    )
])


#run the app
if __name__ == "__main__":
    app.run_server(debug=False)