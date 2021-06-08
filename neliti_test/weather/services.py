import requests

from constant import WEATHER_SERVICE_URL


class WeatherService:
    service_url = WEATHER_SERVICE_URL
    headers = {
        'User-Agent': 'Weather App'
    }

    @classmethod
    def get_weather_info(cls, lat, lon):
        response = requests.get(cls.service_url, params={
            "lat": lat,
            "lon": lon
        }, headers=cls.headers)
        response.raise_for_status()
        return response.json()
