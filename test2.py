from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time 


# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
#chrome_driver = os.getcwd() +"\\chromedriver.exe"
chrome_driver = "/usr/lib/chromium-browser/chromedriver"


# go to Google and click the I'm Feeling Lucky button
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
#driver.get("https://www.google.com")
#lucky_button = driver.find_element_by_css_selector("[name=btnI]")

tic = time.clock()

#driver = webdriver.Chrome(executable_path=chrome_driver)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.nike.com/my/t/zoom-fly-sp-running-shoe-7nfghW/AJ9282-001")


button1 = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'UK 8')]")));
button1.click()

time.sleep(1)

button2 = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'addToCartBtn')]")));
button2.click()

button3 = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Checkout')]")));
button3.click()


# capture the screen
driver.get_screenshot_as_file("capture.png")


toc = time.clock()

ptime = toc - tic

print ('process time: ' , ptime)