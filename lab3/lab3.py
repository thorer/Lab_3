import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st
import streamlit.components.v1 as components

st.title('LAB 2, Noirclerc Thomas')

df = pd.read_csv("oki.csv")
df2 = pd.read_csv("ny-trips-data.csv")
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

df['Date/Time'] = df['Date/Time'].map(pd.to_datetime)
df.head()
def get_dom(dt):
    return dt.day
df['day'] = df['Date/Time'].map(get_dom)
def get_weekday(dt):
    return dt.weekday()
df['weekday']= df['Date/Time'].map(get_weekday)
def get_hour(dt):
    return dt.hour
df['hour'] = df['Date/Time'].map(get_hour)
def count_rows(rows):
    return len(rows)
by_date = df.groupby('day').apply(count_rows)

df3 = df.groupby(['weekday', 'hour']).apply(count_rows).unstack()

df2['tpep_pickup_datetime'] = df2['tpep_pickup_datetime'].map(pd.to_datetime)
df2['tpep_dropoff_datetime'] = df2['tpep_dropoff_datetime'].map(pd.to_datetime)
df2['day_pickup'] = df2['tpep_pickup_datetime'].map(get_dom)
df2['day_dropoff'] = df2['tpep_dropoff_datetime'].map(get_dom)
df2['weekday_pickup']= df2['tpep_pickup_datetime'].map(get_weekday)
df2['weekday_dropoff'] = df2['tpep_dropoff_datetime'].map(get_weekday)
df2['hour_pickup'] = df2['tpep_pickup_datetime'].map(get_hour)
df2['hour_dropoff'] = df2['tpep_dropoff_datetime'].map(get_hour)

def log(func):
    def wrapper(*args,**kwargs):
        with open("test.txt","a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + "at" + str(datetime.datetime.now()) + "\n")
        val = func(*args,**kwargs)
        return val
    
    return wrapper 



option = st.sidebar.selectbox('Select a DataFrame',('Premier DataFrame','Second DataFrame'))

st.header(option)


def option12():
    st.title('Fréquence de commande Uber par jour de la semaine')
    fig1, ax1 = plt.subplots()
    ax1.hist(df.hour, bins = 7, rwidth = 0.8, range = (-0.5, 6.5))
    plt.xlabel('Day of the week')
    plt.ylabel('Frequency')
    plt.title('Frequency by Dom - Uber - April 2014')
    st.pyplot(fig1)

@log        
def option13():   
    st.title('Fréquence de commande Uber par jour du mois')
    fig1, ax1 = plt.subplots()
    ax1.hist(df.day, bins = 30, rwidth = 0.8, range = (0.5, 30.5))
    plt.xlabel('Date of the month')
    plt.ylabel('Frequency')
    plt.title('Frequency by DoM - Uber - April 2014')
    st.pyplot(fig1)

@log
def option14():    
    st.title('Fréquence de commande Uber par heures')
    hour_to_filter=st.slider('Select the hour',min_value=min(df['hour']),max_value=max(df['hour']))
    st.write("Slider:",hour_to_filter)
    filtered_data = df[df["Date/Time"].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    filtered_data['lon'] = df['Lat']
    filtered_data['lat'] = df['Lon']
    st.map(filtered_data)

def option15():   
    st.title('Fréquence de commande Uber par jour de la semaine en heatmap')
    fig, ax = plt.subplots()
    sns.heatmap(df3, ax=ax)
    st.write(fig)

def option16():    
    st.title('Affichage sur une carte')
    components.iframe("https://docs.streamlit.io/en/latest")
    fig, ax = plt.subplots()
    ax.plot(df.Lon, df.Lat, '.', ms = 2, alpha = .5)
    plt.xlim(-74.2, -73.7)
    plt.ylim(40.7, 41)
    plt.grid()
    st.write(fig)

def option11():
    st.title('Fréquence de commande Uber par heures de la journée')
    components.iframe("https://docs.streamlit.io/en/latest")
    fig1, ax1 = plt.subplots()
    ax1.hist(df.hour, bins = 24, range = (0.5, 24))
    plt.xlabel('Hour of the day')
    plt.ylabel('Frequency')
    plt.title('Frequency by Dom - Uber - April 2014')
    st.pyplot(fig1)




def option1():
    st.subheader("Voici le DashBoard du premier DataSet")
    st.title('Voici le premier dataset')
    st.write(df.head(10))
    st.title('Veuillez choisir un histogramme des commandes uber : ')
    select_dataframe = st.radio("Choisissez un histogramme", ('Par heure de la journée','Par jour de la semaine',
'Par Jour du mois', 'En carte et par heure','HeatMap','La totalité sur un carte'))
    if select_dataframe == 'Par heure de la journée':
        option11()
    if select_dataframe == 'Par jour de la semaine':
        option12()
    if select_dataframe == 'Par Jour du mois':
        option13()    
    if select_dataframe == 'Pickup MAP':
        option14()    
    if select_dataframe == 'HeatMap':
        option15()    
    if select_dataframe == 'La totalité sur un carte':
        option16()



if option == 'Premier DataFrame':
    option1()




def option21():
    st.title('Fréquence Prise en charge par heure de la journée')
    fig1, ax1 = plt.subplots()
    plt.hist(df2.hour_pickup, bins = 24, range = (0.5, 24))
    plt.xlabel('Hour of the day for the pickup')
    plt.ylabel('Frequency')
    plt.title('Frequency by Hour for pickup')
    st.pyplot(fig1)
        
def option22():   
    st.title('Affichage sur une carte')
    fig, ax = plt.subplots()
    ax.plot(df2.pickup_longitude, df2.pickup_latitude, '.', ms = 2, alpha = .5)
    plt.xlim(-74.05, -73.75)
    plt.ylim(40.6, 40.98)
    plt.grid()
    st.write(fig)

def option23():    
    st.title('Fréquence Prise arrivé par heure de la journée')
    fig1, ax1 = plt.subplots()
    ax1.hist(df2.hour_dropoff, bins = 24, range = (0.5, 24))
    plt.xlabel('Hour of the day for the dropoff')
    plt.ylabel('Frequency')
    plt.title('Frequency by Hour for dropoff')
    st.pyplot(fig1)

def option24():   
    st.title('Affichage sur une carte des arrivées')
    fig, ax = plt.subplots()
    plt.figure(figsize = (20, 20))
    plt.plot(df2.dropoff_longitude, df2.dropoff_latitude, '.', ms = 2, alpha = .5)
    plt.xlim(-74.05, -73.75)
    plt.ylim(40.6, 40.98)
    plt.grid()
    st.write(fig)

def option25():    
    st.title('Arrivé et prise en charge sur une carte')
    fig, ax = plt.subplots()
    plt.plot(df2.dropoff_longitude, df2.dropoff_latitude, '.', ms = 2, alpha = .5, color = 'r', label = 'dropoff')
    plt.plot(df2.pickup_longitude, df2.pickup_latitude, '.', ms = 2, alpha = .5, color = 'b', label = 'pickup')
    plt.xlim(-74.05, -73.75)
    plt.ylim(40.6, 40.98)
    plt.grid()
    st.write(fig)




def option2():
    st.subheader("Voici le DashBoard du second DataSet")
    st.title('Voici le deuxième dataset')
    st.write(df2.head(10))
    st.title('Veuillez choisir un histogramme des commandes uber : ')
    select_dataframe = st.radio("Choisissez un histogramme", ('Prise en charge par heure de la journée','La totalité sur un carte des prises en charges',
'Arrivé par heure de la journée','La totalité sur un carte des arrivées','Arrivé et prise en charge sur une carte'))
    if select_dataframe == 'Prise en charge par heure de la journée':
        option21()
    if select_dataframe == 'La totalité sur un carte des prises en charges':
        option22()
    if select_dataframe == 'Arrivé par heure de la journée':
        option23()    
    if select_dataframe == 'La totalité sur un carte des arrivées':
        option24()    
    if select_dataframe == 'Arrivé et prise en charge sur une carte':
        option25() 



if option == 'Second DataFrame':
    option2()


    