from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
submit = driver.find_element(By.ID, 'login-button')
if username and password and submit is None:
    print("Элементы не найдены")
else:
    print("Элементы найдены")