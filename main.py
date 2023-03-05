import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Up to Five Days")
place = st.text_input("Place:", help="Type the city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days", step=1)
option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the following {days} day(s) in {place}")


def get_data(days):
    dates = ["2023-03-05", "2023-03-06", "2023-03-07"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Data", "y": "Temperature (C)"})
st.plotly_chart(figure)
