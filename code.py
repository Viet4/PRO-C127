from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('./chromedriver.exe')
browser.get(start_url)

time.sleep(10)

headers = [
    "Name", 
    "Distance", 
    "Mass",
    "Radius"
]
stars_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")

temp_list = []
for tr_tag in soup.find('table').find_all("tr"):
    td_tags = tr_tag.find_all("td")

    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

for i in range(1, len(temp_list)):
    stars_data.append([
        temp_list[i][1], 
        temp_list[i][3], 
        temp_list[i][5], 
        temp_list[i][6]
        ])

with open("scrapper.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)