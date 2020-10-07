from pprint import pprint
import requests
import os

key = os.environ.get('WEATHER_KEY')
url = f'http://api.openweathermap.org/data/2.5/weather'

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Location not found.')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp} C')

# Getting a valid location (city and country 2letter code)
def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input('Please enter the city: ').strip()

    while len(country) !=2 or not country.isalpha():
        country = input('Enter the 2 letter country code: ')
    location = f'{city}, {country}'
    return location

# quiery is used to keep the code cleaner and orginized using the url and location mentiones above
def get_current_weather(location, key):
    #added a try exceptio to catch errors the 
    #weather temp, caused by either location or key
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key }
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex
    
# getting current weather and displaying so code is readable for user 
def get_temp(weather_data):
    
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'

if __name__ == "__main__":
    main()



#06bc43fe0ae331aad85e292c16442f95