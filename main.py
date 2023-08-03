import requests

# url = \
#     "http://api.openweathermap.org/data/2.5/forecast?q=Madrid&appid=fb026b1b1f2f3bf02874a165e116af7e&units=metric"
# r = requests.get(url)
# print(r.json())

url = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}"

class Weather:

    def __init__(self, apikey, city = None, lat = None, lon = None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
            # print(self.data)
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("You must specify either a city or a latitude and longitude")
        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12_hours(self):
        return self.data["list"][:4]

    def next_12_hours_simplified(self):
        simple_data = []
        for dicty in self.data["list"][:4]:
            simple_data.append((dicty["dt_txt"], dicty["main"]["temp"], dicty["weather"][0]["description"]))
            return simple_data
        # return (self.data["list"][0]["dt_txt"], self.data["list"][0]["main"]["temp"], self.data["list"][0]["weather"][0]["description"])

weather = Weather(apikey="fb026b1b1f2f3bf02874a165e116af7e", city=  "Madrid",  lat = 4.1, lon = 4.5)
print(weather.next_12_hours_simplified())
