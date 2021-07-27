import json
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('counties.html', encoding='utf8'), 'html.parser')

paths = soup.find_all('path', class_='county-boundary')

county_json = []

for path in paths:
  
  try: 
    fill = path.attrs.get('style').split('fill: ')[1]
    transmission_level = ''

    if fill == 'rgb(255, 247, 14);':
      transmission_level = 'moderate'
    elif fill == 'rgb(255, 0, 0);': 
      transmission_level = 'high'
    elif fill == 'rgb(255, 113, 52);': 
      transmission_level = 'substantial'
    elif fill == 'rgb(29, 138, 255);':
      transmission_level = 'low'
    else: 
      transmission_level = 'na'

    mask = "Mask"

    if transmission_level == 'moderate' or transmission_level == 'low':
        mask = "No Mask"

    if transmission_level == 'na':
        mask = 'Not available'
  except IndexError:
      transmission_level = 'na'
      mask = 'Not available'



  county = {
    "name": path.attrs.get('data-county'),
    "state": path.attrs.get('data-state'),
    "fips": path.attrs.get('data-fips'),
    "fill": fill,
    "transmission_level": transmission_level,
    "mask": mask
  }

  county_json.append(county)

with open("formatted.json", "w") as data_file:
  json.dump(county_json, data_file)