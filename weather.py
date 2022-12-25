import requests, json


class Weather:
    def __init__(self, key, location):
        self.key = key
        self.location = location
    
    
    def get_current_weather(self):
        base_url = ("http://api.weatherapi.com/v1/current.json?lang=de&"
                   f"key={self.key}&q={self.location}")
        res = requests.get(base_url)
        return res
    
    
    def get_current_temperatur(self):
        current_weather = self.get_current_weather()
        data = json.loads(current_weather.text)
        return data["current"]["temp_c"]