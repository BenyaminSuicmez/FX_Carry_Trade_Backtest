# This file serves the purpose of downloading data and storing it in "/data"
import requests


def download():
    url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_KEI@DF_KEI,/AUS+CAN+JPN+NZL+NOR+SWE+CHE+GBR+USA+EA20.Q.IR3TIB.PA._Z..?startPeriod=2015-Q1&endPeriod=2025-Q4&dimensionAtObservation=AllDimensions&format=csvfilewithlabels"
    path = "data/oecd_ir3tib_2015_2025.csv"

    response = requests.get(url=url)
    response.raise_for_status() # Checking the connection of the API

    with open(path, "w", encoding="utf-8") as file:
        file.write(response.text)
    