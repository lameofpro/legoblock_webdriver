from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up drivers
#driverDir = "chromedriver.exe"
#driver = webdriver.Chrome(executable_path=driverDir)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to Google Webpage
driver.get("https://www.google.com/")
try:
    searchBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )                               # Wait until the search bar exist
    searchBox.clear()               # Clear any existing input
    searchBox.send_keys("lego")     # Search for lego
except:
    print("ERROR: cannot search for lego.")

