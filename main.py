import streamlit as st

st.title("Weather Forecast for Up to Five Days")
place = st.text_input("Place:", help="Type the city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days", step=1)
option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the following {days} day(s) in {place}")
