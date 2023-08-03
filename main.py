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
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            print("Error: No city or lat lon provided")

    def next_12_hours(self):
        return self.data["list"][:4]

    def next_12_hours_simplified(self):
        pass

weather = Weather(apikey="fb026b1b1f2f3bf02874a165e116af7e", lat = 4.1, lon = 4.5)
print(weather.next_12_hours())
