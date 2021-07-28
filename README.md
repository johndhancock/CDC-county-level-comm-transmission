[![cdc-data-scraper](https://github.com/johndhancock/CDC-county-level-comm-transmission/actions/workflows/scraper.yml/badge.svg)](https://github.com/johndhancock/CDC-county-level-comm-transmission/actions/workflows/scraper.yml)

# CDC-county-level-comm-transmission

This is a quick cleaner file that takes the svg element of the [CDC's county level community transmission level map](https://covid.cdc.gov/covid-data-tracker/#county-view) and parses the data into a structured format using the data attributes on the individual county paths.

## How to use

- Download the repo and run `pipenv install`.
- Copy the `g id=counties` element from the CDC's map and paste the contents into `counties.html`
- Run `pipenv run python cleaner.py` to output the data into a json format. The csv included was manually produced for the first day using a json-to-csv converter online. 

