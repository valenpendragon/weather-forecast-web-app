import os
import requests


def get_data(place: str, forecast_days=1):
    """This function uses place to determine the location for the weather
    data, forecast_days for the number of days to return, and data_type
    for the structure or appearance of the data: graphical p[otting of
    the expected temperatures or icons for the type of weather, such as
    partly cloudy, rain, etc. This data is accumulated and returned to the
    calling program.
    :return: data
    """
    api_key = os.getenv("WMORG_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
          f"&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    no_data_values = 8 * forecast_days
    try:
        filtered_data = data["list"][:no_data_values]
    except KeyError:
        return None
    else:
        return filtered_data


if __name__ == "__main__":
    print(get_data("pickerington", forecast_days=3))