from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = r"C:\\Program Files\\chromedriver_win32\\chromedriver.exe"

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.ea.com/en-gb/fifa/ultimate-team/web-app/")
time.sleep(15)

# Add the xpath of the element here, using the 'By' imported function
# Potential values
# /html/body/main/div/div/div/button[1]
# //*[@id="Login"]/div/div/button[1]
driver.find_element

print(driver.page_source)
driver.quit()
