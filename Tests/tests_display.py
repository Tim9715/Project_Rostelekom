import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Data.driver_data import *
from Data.valid_data import *

def test_display_auth_form():
    """Проверка отображения формы "Авторизация" """
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    Tabs_menu = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]')
    Tabs = driver.find_elements(By.CLASS_NAME, 'rt-tab--small')
    Form_login = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input')
    Form_pass = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input')

    assert Tabs_menu and len(Tabs) == 4 and Form_login and Form_pass

    driver.quit()

def test_display_auth_logo():
    """Проверка отображения логотипа на странице авторизации"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    Logo = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]')
    Info = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[2]')

    assert Logo and Info

    driver.quit()

def test_clickability_tabs():
    """Проверка кликабельности табов в меню выбора аутентификации"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)
    
    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')
    assert 'Телефон' == active_tab.text

    Tab_post = driver.find_element(By.ID, 't-btn-tab-mail').click()

    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')
    assert 'Почта' == active_tab.text

    Tab_login = driver.find_element(By.ID, 't-btn-tab-login').click()

    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')
    assert 'Логин' == active_tab.text

    Tab_ls = driver.find_element(By.ID, 't-btn-tab-ls').click()

    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')
    assert 'Лицевой счёт' == active_tab.text

    Tab_phone = driver.find_element(By.ID, 't-btn-tab-phone').click()

    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')
    assert 'Телефон' == active_tab.text

    driver.quit()

def test_auto_switch_tab():
    """Проверка авто переключения табов во время заполнения"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')

    assert 'Телефон' == active_tab.text

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input')
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input')

    login_field.send_keys(email1)
    password_field.click()
    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')

    assert 'Почта' == active_tab.text

    login_field.send_keys(Keys.CONTROL + 'a')
    login_field.send_keys(Keys.DELETE)

    login_field.send_keys(login1)
    password_field.click()
    active_tab = driver.find_element(By.CLASS_NAME, 'rt-tab--active')

    assert 'Логин' == active_tab.text

    driver.quit()

def test_display_password_recovery_form():
    """Проверка отображения формы "Восстановление пароля" """
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    forgot_pass_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/a').click()

    Tabs_menu = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]')
    Tabs = driver.find_elements(By.CLASS_NAME, 'rt-tab--small')
    Form_login = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input')
    Form_captcha = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div[2]/div/input')
    Button_continue = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button[1]')
    Button_return = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button[2]')

    assert Tabs_menu and Tabs and Form_login and Form_captcha and Button_continue and Button_return

    driver.quit()

def test_display_password_recovery_logo():
    "Проверка отображения логотипа на странице восстановления пароля"
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    forgot_pass_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/a').click()

    Logo_Info = driver.find_element(By.CLASS_NAME, 'what-is-container')

    assert Logo_Info

    driver.quit()

def test_display_reg_form():
    """Проверка отображения формы "Регистрация" """
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    button_reg = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    field_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input')
    field_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input')
    field_region = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input')
    field_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/div/input')
    field_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/div/input')
    field_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input')
    button_registration = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button')
    link = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[5]/a')

    assert field_name and field_surname and field_region and field_email_or_number and field_password and field_confirm_password and button_registration and link

    driver.quit()

def test_display_reg_logo():
    """Проверка отображения логотипа на странице регистрации"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    button_reg = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    Logo_Info = driver.find_element(By.CLASS_NAME, 'what-is-container')

    assert Logo_Info

    driver.quit()
