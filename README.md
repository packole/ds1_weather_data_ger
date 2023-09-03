  ## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)

### General Info

This repository is a data science project with following project goals:

  - visualize historical weather data of diffrent german cities
  - input data should be transformed and stored in a .csv file
  - data should not be automatically updated
  - data transformation should be written in python
  - a data application with plotly dash should be developed to local host
 

The project can be devided into different steps wich are explaned in the following:

step 1: data collecting 
  - the required data must be extracted from a suitable source
  - no special criteria are set for data quantity and quality

step 2: data preparation and transformation
  - exploring the collected data
  - transformation of the data for usage in data app
  - if there is a really bad data quality return to step 1

step 3: data application
  - development of a data app with ploty dash framework
  - local hosting and deployment of the app via flask
  - if there are transformation missed return to step 2

## Technologies
***
A list of technologies used within the project:
* [GitHub](https://github.com/packole/ds1_weather_data_ger)
* [Python](https://www.python.org/): Version 3.10.12
* [Dash](https://plotly.com/): Version 2.12.1
* [Pandas](https://pandas.pydata.org/): Version 2.0.3
* [matplotlib](https://matplotlib.org/): Version 3.7.2
* [Ubuntu](https://ubuntu.com/): Version 22.04.3 LTS

## Installation (tbd.)
***
A little intro about the installation: 

(The following instructions apply to Windows command line.)

To run this app first clone repository and then open a terminal to the app folder.

'
git clone https://github.com/packole/ds1_weather_data_ger
cd dash-sample-apps/apps/dash-uber-rides-demo
'


Create and activate a new virtual environment (recommended) by running the following:

On Windows
'
virtualenv venv 
\venv\scripts\activate
'

Or if using linux
'
python3 -m venv myvenv
source myvenv/bin/activate
'

Install the requirements:
'
pip install -r requirements.txt
'

Open IDE and edit data path in own path

Run the app:
'
dash_app.py
'

You can run the app on your browser at http://127.0.0.1:8050

## Collaboration
***
In case of a desired collaboration or feeback please feel free to contact us at phillip.ackermann@protonmail.com or here in GitHub.com.