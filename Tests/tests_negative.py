import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Data.driver_data import *
from Data.valid_data import *
from Data.invalid_data import *

def test_auth_number_invalid_login():
    """Проверка авторизации с неправильным номером, но правильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(inv_number)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_number_invalid_password():
    """Проверка авторизации с правильным номером, но неправильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(number1)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(inv_password)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_number_empty_form():
    """Проверка ввода пустой формы в авторизации по номеру"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    orange_field = driver.find_element(By.CLASS_NAME, 'rt-input-container--error')
    error_message = driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    assert orange_field and error_message.text == 'Введите номер телефона'

    driver.quit()

def test_auth_email_invalid_login():
    """Проверка авторизации с неправильной электронной почтой, но правильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(inv_email)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_email_invalid_password():
    """Проверка авторизации с правильной электронной почтой, но неправильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(email1)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(inv_password)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_email_empty_form():
    """Проверка ввода пустой формы в авторизации по электронной почте"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    Tab_post = driver.find_element(By.ID, 't-btn-tab-mail').click()

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    orange_field = driver.find_element(By.CLASS_NAME, 'rt-input-container--error')
    error_message = driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    assert orange_field and error_message.text == 'Введите адрес, указанный при регистрации'

    driver.quit()

def test_auth_login_invalid_login():
    """Проверка авторизации с правильным логином, но неправильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(inv_login)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_login_invalid_password():
    """Проверка авторизации с неправильным логином, но правильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(login1)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(inv_password)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_login_empty_form():
    """Проверка ввода пустой формы в авторизации по логину"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    Tab_login = driver.find_element(By.ID, 't-btn-tab-login').click()

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    orange_field = driver.find_element(By.CLASS_NAME, 'rt-input-container--error')
    error_message = driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    assert orange_field and error_message.text == 'Введите логин, указанный при регистрации'

    driver.quit()

def test_auth_LS_invalid_login():
    """Проверка авторизации с неправильным номером лицевого счётом, но правильным паролем"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    LS_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[4]').click()

    login_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys(inv_LS)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/input').send_keys(password1)

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.ID, 'form-error-message')
    forgot_pass = driver.find_element(By.CLASS_NAME, 'login-form__forgot-pwd--animated')

    assert error_message.text == 'Неверный логин или пароль' and forgot_pass

    driver.quit()

def test_auth_LS_empty_form():
    """Проверка ввода пустой формы в авторизации по номеру лицевого счёта"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    Tab_ls = driver.find_element(By.ID, 't-btn-tab-ls').click()

    auth_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    orange_field = driver.find_element(By.CLASS_NAME, 'rt-input-container--error')
    error_message = driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    assert orange_field and error_message.text == 'Введите номер вашего лицевого счета'

    driver.quit()

def test_reg_empty_form():
    """Проверка ввода пустой формы в регистрации"""
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    reg_link = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    time.sleep(3)

    reg_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span')
    error_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span')
    error_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/span')
    error_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span')
    error_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/span')

    assert error_name and error_surname and error_email_or_number and error_password and error_confirm_password

    driver.quit()

def test_reg_mismatch_password():
    """Проверка несовпадения паролей"""
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
    field_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input').send_keys(inv_password)

    button_registration = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    error_message = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/span')

    assert error_message.text == 'Пароли не совпадают'

    driver.quit()

def test_non_unique_data_registration_email():
    """Проверка ввода неуникальных данных при регистрации по электронной почте"""
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

    error_card = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div/div')

    assert error_card

    driver.quit()

def test_non_unique_data_registration_number():
    """Проверка ввода неуникальных данных при регистрации по номеру"""
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

    error_card = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div/div')

    assert error_card

    driver.quit()

def test_no_valid_name_and_email_or_number():
    """Проверка валидности полей "Имя" и "Электронная почта или номер" """
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    reg_link = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    field_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input')
    field_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input')

    field_name.send_keys(big_name)
    field_surname.click()
    error_message_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span')
    assert error_message_name

    field_name.send_keys(Keys.CONTROL + 'a', Keys.DELETE)

    field_name.send_keys(little_name)
    field_surname.send_keys(surname1)
    error_message_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span')
    assert error_message_name

    field_region = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input')
    field_region.click()
    field_region.send_keys(Keys.CONTROL + 'a', Keys.DELETE, region1)
    field_select = driver.find_element(By.CLASS_NAME, 'rt-select__list-wrapper').click()

    field_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/div/input')
    field_email_or_number.send_keys(big_number)
    field_surname.click()
    error_message_email_or_number = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/span')
    assert error_message_email_or_number

    field_email_or_number.send_keys(Keys.CONTROL + 'a', Keys.DELETE)

    field_email_or_number.send_keys(big_email)
    field_surname.click()
    error_message_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/span')
    assert error_message_email_or_number

    field_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/div/input').send_keys(password1)
    field_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input').send_keys(password1)

    button_registration = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    driver.quit()

def test_no_valid_surname_and_password():
    """Проверка валидности полей "Фамилия" и "Пароль" """
    driver = webdriver.Chrome(driver1)
    driver.get(url1)

    time.sleep(6)

    reg_link = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[6]/a').click()

    field_name = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input')
    field_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input')

    field_surname.send_keys(big_surname)
    field_name.click()
    error_message_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span')
    assert error_message_surname

    field_surname.send_keys(Keys.CONTROL + 'a', Keys.DELETE)

    field_surname.send_keys(little_surname)
    field_name.send_keys(name1)
    error_message_surname = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span')
    assert error_message_surname

    field_region = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input')
    field_region.click()
    field_region.send_keys(Keys.CONTROL + 'a', Keys.DELETE, region1)
    field_select = driver.find_element(By.CLASS_NAME, 'rt-select__list-wrapper').click()

    field_email_or_number = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/div/input').send_keys(email1)

    field_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/div/input')
    field_confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/div/input')

    field_password.send_keys(big_password)
    field_confirm_password.click()
    error_message_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span')
    assert error_message_password

    field_password.send_keys(Keys.CONTROL + 'a', Keys.DELETE)

    field_password.send_keys(little_password)
    field_confirm_password.click()
    error_message_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span')
    assert error_message_password

    field_password.send_keys(Keys.CONTROL + 'a', Keys.DELETE)

    field_password.send_keys(down_password)
    field_confirm_password.click()
    error_message_password = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span')
    assert error_message_password

    button_registration = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/button').click()

    driver.quit()
