import streamlit as st
import requests

api_key = "f194150c77ff473ae8c012eb951efeab"
st.title("🌞 Weather Forecast")
city = st.text_input("Please enter city name or ZIP code: ")


unit = st.radio("Choose temperature unit: Celsius or Fahrenheit?", ["Celsius", "Fahrenheit"])

if st.button("Get Current Weather Forecast"):
    if not city:
        st.warning("Please enter city name or ZIP code")
    else:
        url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
        response = requests.get(url)
        data = response.json()

        if data.get("error"):
            st.warning("Location not found.")
        else:
            temperature = data["current"]["temperature"]
            weather_description = data["current"]["weather_descriptions"][0]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_speed"]
            if unit == "Fahrenheit":
                temperature = (temperature * 9/5) + 32
            
            st.write("🌡️ Temperature: ", temperature, unit)
            st.write("🌤️ Weather description: ", weather_description)
            st.write("💦 Humidity: ", humidity, "%")
            st.write("💨 Wind speed: ", wind_speed, "km/h")

