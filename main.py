import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Up to Five Days")
place = st.text_input("Place:", help="Type the city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days", step=1)
option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the following {days} day(s) in {place}")

data = get_data(place, days, option)

# d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Data", "y": "Temperature (C)"})
st.plotly_chart(figure)
