import streamlit as st
import plotly.express as px
from backend import get_data

# Icon to Path dictionary.
ICONS = {
    "Rain": "icons/4 Cloud Rain.png",
    "Drizzle": "icons/4 Cloud Rain.png",
    "Snow": "icons/7 Cloud Snow.png",
    "Thunderstorm ": "icons/10 Cloud Lightning.png",
    "Clouds": "icons/20 Clouds.png",
    "Mist": "icons/20 Clouds.png",
    "Haze": "icons/24 Cloud Fog.png",
    "Fog": "icons/24 Cloud Fog.png",
    "Dust": "icons/24 Cloud Fog.png",
    "Smoke": "icons/24 Cloud Fog.png",
    "Ash": "icons/24 Cloud Fog.png",
    "Sand": "icons/24 Cloud Fog.png",
    "Squall": "icons/36 Cloud Lightning.png",
    "Clear": "icons/54 Sun.png",
    "Tornado": "icons/102 Tornado.png"
}

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for Up to Five Days")
place = st.text_input("Place:", help="Type the city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecasted days", step=1)
option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the following {days} day(s) in {place.title()}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)
    if filtered_data:
        temps = [dict["main"]["temp"] for dict in filtered_data]
        conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]

        if option == "Temperature":
            # Create temperature plot
            figure = px.line(x=dates, y=temps, labels={"x": "Data", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Create sky conditions output
            image_paths = [ICONS[condition] for condition in conditions]
            st.image(image_paths, caption=dates)
    else:
        st.write(f"{place} was not found in available weather data.")
        st.write("Double check the spelling and try again.")