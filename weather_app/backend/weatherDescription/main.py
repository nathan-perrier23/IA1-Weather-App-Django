import requests
from decouple import config
import json

from .__init__ import WeatherCodeDesc

class GetWeatherDescription():
    def __init__(self, location):
        self.location = location
        self.weather_code_desc = WeatherCodeDesc
        
    def get_weather_description(self):
        ''' returns a weather description '''
        try:
            return self.weather_code_desc[str(self.get_weather_code())]
        except KeyError: return 'Unknown'
        
    def get_weather_code(self):
        ''' returns a weather code '''
        try:
            url = f'https://api.tomorrow.io/v4/timelines?apikey={config("TOMORROWIO_API_KEY")}'
            headers = {
                'Accept-Encoding': 'gzip',
                'accept': 'application/json',
                'content-type': 'application/json',
            }
            data = {
                "location": self.location.city,
                "fields": ['weatherCode'],
                "units": 'metric',
                "timesteps": ['current'],
                "timezone": self.location.timezone
            }

            response = requests.post(url, headers=headers, data=json.dumps(data)).json()
            return response['data']['timelines'][0]['intervals'][0]['values']['weatherCode']
        except: return '1000'