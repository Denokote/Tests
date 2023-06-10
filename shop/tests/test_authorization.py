from selenium.webdriver.common.by import By
from shop.data.data import base_url, password, email
from shop.secondary_functions.waiting_elements import wait_vs as wvs
from datetime import datetime
import pickle
from shop.main import start
import time


def test_autorization() -> None:
    try:
        driver = start()
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
            pickle.dump(driver.get_cookies(), open('shop/tests/cookies/' + f'{str(datetime.now())[:-16]}_cookies',
                                                   'wb'))
        else:
            message = 'Тест авторизации ПРОВАЛЕН\n'

        assert res == 'Денис'

    except Exception as ex:
        message = 'Тест авторизации: ' + ex.__str__()
        raise ex

    finally:
        with open('shop/tests/logs/' + f'{str(datetime.now())[:-12]}XX_log.txt', 'a') as file:
            file.write(f'{message}')
        driver.close()
        driver.quit()
        time.sleep(2)
