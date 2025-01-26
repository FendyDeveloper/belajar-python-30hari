import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#
# data = response.json()
# print(data)

MY_LAT = -7.47056
MY_LONG = 110.21778

parameters = {
    'lat' = MY_LAT,
    'long' = MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json)
print(response.status_code)
print(response.text)
