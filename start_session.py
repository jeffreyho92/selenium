from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time 

chrome_driver = "/usr/lib/chromium-browser/chromedriver"

prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://google.com")

print session_id
print executor_url
'''
session_id = "0f3cf15f8e85e0fd9f7ca80c1b46c1ac"
executor_url = "http://127.0.0.1:44497"

driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver.session_id = session_id
driver.get("http://google.com")
print driver2.current_url
'''

input("Press Enter to Exit...")