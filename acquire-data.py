#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import os
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

"""
This script is the first step in the process
to pull down a copy of the county-level json
used to power the CDC's Covid-19 dashboard
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_json = "daily-json"

file_output = '{0}-cdc-daily-county.json'.format(timestamp)

file_saved = os.path.join(dir_current, dir_json, file_output)

target_url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=integrated_county_latest_external_data"

response = requests.get(target_url)

data = json.loads(response.text)

with open(file_saved, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

logger.debug('File saved to {0}'.format(file_saved))
