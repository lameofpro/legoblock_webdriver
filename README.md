# Lego-block: Webdriver
This lego block focus on automatic controlling a web browser from Python. This is handy when working with website like wordpress to upload contents from a database or testing a website.

# Installation
This webdriver is run by Selenium Library, which can be install by
```
pip install selenium
```
A web broswer driver is needed to provide the navigation. There are two known methods for the installation:
## Hard Coded Location
Choose a web broswer to use, and download a drive from [this website](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).
> Make sure the downloaded driver's verion match your web browser version.

```
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)
```
## Driver Management Software
1. Import driver
```
from webdriver_manager.chrome import ChromeDriverManager
```
2. Get location
```
service = Service(executable_path=ChromeDriverManager().install())
```
3. Use Service instance
```
driver = webdriver.Chrome(service=service)
```
