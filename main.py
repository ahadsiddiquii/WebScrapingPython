import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=29.1737&lon=-94.9872#.YD40DygzbIU')
soup = BeautifulSoup(page.content, 'html.parser')

weekly_panel_title = soup.find(id='seven-day-forecast')
panel_desc = weekly_panel_title.find('b').get_text()
panel_location = weekly_panel_title.find(class_='panel-title').get_text()
a_list = panel_location.split()
panel_location = " ".join(a_list)

weekly_forecast = soup.find(id='seven-day-forecast-body')
items = weekly_forecast.find_all(class_='tombstone-container')
period_name = list()
short_desc = list()
temperature = list()

# period_name = [item.find(class_='period-name').get_text() for item in items]

for item in items:
    period_name.append(item.find(class_='period-name').get_text())
    short_desc.append(item.find(class_='short-desc').get_text())
    temperature.append(item.find(class_='temp').get_text())

print('\n' + panel_desc + " " + panel_location + '\n')
# for list_item in range(0, 9):
#     print(period_name[list_item] + ", " + short_desc[list_item] + ", " + temperature[list_item])

weekly_weather_forecast = pd.DataFrame(
    {
        'period': period_name,
        'short_description': short_desc,
        'temperature': temperature,
    }
)

print(weekly_weather_forecast)
weekly_weather_forecast.to_csv('weekly_weather.csv')

