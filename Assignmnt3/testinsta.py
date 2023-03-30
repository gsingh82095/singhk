from selenium import webdriver
import time

# Set path of chromedriver
driver_path = "C:/Selenium browser drivers/chromedriver.exe"

# Create Chrome driver object
driver = webdriver.Chrome(executable_path=driver_path)

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for page to load
time.sleep(5)

# Quit the driver and close all windows
driver.quit()
