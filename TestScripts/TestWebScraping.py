import timeit

import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd

driver_path = 'msedgedriver.exe'

constituents_url = 'https://www.stoxx.com/index-details?symbol=SXXP'

table_id = "stoxx_index_detail_component"

constituents = {}

driver = webdriver.Edge(driver_path)
driver.get(url=constituents_url)

components = driver.find_element_by_link_text('Components')
components.click()

driver.implicitly_wait(2)

table = driver.find_element_by_id('component-table')
for row in table.find_elements_by_xpath(".//tr"):
    try:
        href = row.find_element_by_xpath("./td[1]/input")
        constituents[row.text] = href.get_property('value')
    except:
        # TODO: Add Logger
        continue

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]'))).click()

button_list = driver.find_elements_by_xpath("//*/li[contains(@onclick,'paginate')]")
counter = len(button_list)
driver.implicitly_wait(2)
idx = 0
while idx < counter:
    print("Loading page {0}".format(idx))

    button_list = driver.find_elements_by_xpath("//*/li[contains(@onclick,'paginate')]")
    button_list[idx].click()

    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'component-table')))
    table = driver.find_element_by_id('component-table')
    rows = table.find_elements_by_xpath(".//tr")

    print(len(rows))
    for row in rows:
        driver.implicitly_wait(2)
        try:
            href = row.find_element_by_xpath("./td[1]/input")
            constituents[row.text] = href.get_property('value')
        except Exception as err:
            print("Issue: {0}".format(err))# TODO: Add Logger
            driver.implicitly_wait(2)
            continue

    idx = idx+1

href = constituents.popitem()[1]
driver.get(href)
table = driver.find_element_by_class_name('flat-table')
static_data = table.text.split('\n')

output = []
for key_value in static_data:
    key, value = key_value.split(': ', 1)
    if not output or key in output[-1]:
        output.append({})
    output[-1][key] = value