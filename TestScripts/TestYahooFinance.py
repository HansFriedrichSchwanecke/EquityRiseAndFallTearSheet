from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = 'msedgedriver.exe'

fundamentals_url = 'https://finance.yahoo.com/'

driver = webdriver.Edge(driver_path)
driver.get(fundamentals_url)