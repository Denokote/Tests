from selenium.webdriver.common.by import By
from data import base_url, password, email
from secondary_functions.waiting_for_visible_element import wait_vs as wvs
from datetime import datetime


def test_autorization(driver):
    try:
        driver.get(base_url)
        wvs(driver, 'CSS', 'div[class*=header-user-wrapper]').click()

        email_input = wvs(driver, 'ID', 'user_email')
        email_input.clear()
        email_input.send_keys(email)
        driver.find_element(By.ID, 'enter-id-submit').click()

        password_input = wvs(driver, 'ID', 'user_password')
        password_input.clear()
        password_input.send_keys(password)
        driver.find_element(By.ID, 'link_login').click()

        driver.refresh()
        res = wvs(driver, 'CSS', 'div[class*=header-user-wrapper]').text
        if res == 'Денис':
            message = 'Тест авторизации выполнен успешно\n'
        else:
            message = 'Тест авторизации ПРОВАЛЕН\n'

    except Exception as ex:
        message = ex
    finally:
        with open('logs/' + f'{str(datetime.now())[:-10]}_log.txt', 'a') as file:
            file.write(f'{message}')
        driver.close()
        driver.quit()
