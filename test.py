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

#disable image loading
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)


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
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
#driver.get("https://www.nike.com/my/t/zoom-fly-sp-running-shoe-7nfghW/AJ9282-001")



session_id = "0f3cf15f8e85e0fd9f7ca80c1b46c1ac"
executor_url = "http://127.0.0.1:44497"

driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver.session_id = session_id
driver.get("https://store.nike.com/my/en_gb/pd/vaporfly-4-flyknit-running-shoe/pid-12249650/pgid-12440409")
'''
def until_func(driver):
  print 'refresh'
  driver.refresh()
  EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'UK 7')]"))

button1 = WebDriverWait(driver, timeout=60, poll_frequency=10).until(until_func)
button1.click()
'''

timeout1 = 20
timeout2 = 10

print 'button1 start'
button1 = WebDriverWait(driver, timeout1).until(
EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'UK 8')]")));
button1.click()
print 'button1 end'
#time.sleep(1)

print 'button2 start'
button2 = WebDriverWait(driver, timeout2).until(
EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'addToCartBtn')]")));
button2.click()
print 'button2 end'

print 'button3 start'
button3 = WebDriverWait(driver, timeout2).until(
EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Checkout')]")));
button3.click()
print 'button3 end'


# capture the screen
driver.get_screenshot_as_file("capture.png")


toc = time.clock()

ptime = toc - tic

print ('process time: ' , ptime)