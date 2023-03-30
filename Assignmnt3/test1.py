from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver.exe")
browser.get("https://www.saucedemo.com/")

# Enter the credentials and login
username = browser.find_element(By.ID, "user-name")
username.send_keys("standard_user")
password = browser.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login_button = browser.find_element(By.ID, "login-button")
login_button.click()

# Wait for the products page to load and check for the presence of four elements
wait = WebDriverWait(browser, 10)
products_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_label")))
cart_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_container")))
menu_button = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
logout_button = wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))

print("All elements are present on the page.")

browser.quit()