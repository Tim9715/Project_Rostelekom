import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Data.driver_data import *
from Data.valid_data import *

def test_successfully_auth_number():
    """Проверка успешной авторизации номеру"""

    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(number1)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    time.sleep(3)

    test_auth_text = driver.find_element(By.CLASS_NAME, 'card-title')

    assert test_auth_text

    driver.quit()

def test_successfully_auth_email():
    """Проверка успешной авторизации по электронной почте"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(email1)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    time.sleep(3)

    test_auth_text = driver.find_element(By.CLASS_NAME, 'card-title')

    assert test_auth_text

    driver.quit()

def test_successfully_auth_login():
    """Проверка успешной авторизации по логину"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(login1)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    time.sleep(3)

    test_auth_text = driver.find_element(By.CLASS_NAME, 'card-title')

    assert test_auth_text

    driver.quit()

def test_successfully_registration_email():
    """Проверка успешной регистрации по электронной почте"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    reg_link = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    field_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input').send_keys(name1)
    field_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(surname1)

    field_region = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input')
    field_region.click()
    field_region.send_keys(Keys.CONTROL + 'a', Keys.DELETE, region1)
    field_select = driver.find_element(By.CLASS_NAME, 'rt-select__list-wrapper').click()

    field_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/div/input').send_keys(email1)

    field_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/div/input').send_keys(password1)
    field_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input').send_keys(password1)

    button_registration = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    driver.quit()

def test_successfully_registration_number():
    """Проверка успешной регистрации по номеру"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    reg_link = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    field_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input').send_keys(name1)
    field_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(surname1)

    field_region = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input')
    field_region.click()
    field_region.send_keys(Keys.CONTROL + 'a', Keys.DELETE, region1)
    field_select = driver.find_element(By.CLASS_NAME, 'rt-select__list-wrapper').click()

    field_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/div/input').send_keys(number1)

    field_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/div/input').send_keys(password1)
    field_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input').send_keys(password1)

    button_registration = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    driver.quit()