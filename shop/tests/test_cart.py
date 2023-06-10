from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from shop.main import start
from shop.data.data import base_url
from shop.secondary_functions.waiting_elements import wait_vs as wvs, wait_all_vs as wavs
from random import choice
import pickle
from datetime import datetime
import time


def test_cart() -> None:
    try:
        driver = start()
        driver.get(base_url)

        with open('shop/tests/cookies/' + f'{str(datetime.now())[:-16]}_cookies', 'rb') as cookies:
            for cookie in pickle.load(cookies):
                driver.add_cookie(cookie)

        driver.refresh()
        wvs(driver, 'CSS', 'a[class*=header-catalog-btn]').click()

        wavs(driver, 'CSS', 'div[class=group-list]')
        categories_list = driver.find_elements(By.CLASS_NAME, 'head-4')
        time.sleep(1)
        choice(categories_list).click()

        wavs(driver, 'CSS', 'li[class*=group-list-item]')
        subcategories_list = driver.find_elements(By.CSS_SELECTOR, 'li[class*=group-list-item]')
        time.sleep(1)
        choice(subcategories_list).click()

        wavs(driver, 'CSS', 'li[class*=box-inline]')
        goods_list = driver.find_elements(By.CSS_SELECTOR, 'li[class*=box-inline]')[:-5]
        goods = choice(goods_list)
        time.sleep(1)

        while goods.find_element(By.CSS_SELECTOR, 'div[class*=new-item-list-btn]').text != 'В корзину':
            goods = choice(goods_list)

        goods_name = goods.find_element(By.CSS_SELECTOR, 'div[class*=new-item-list-name]').text
        goods.find_element(By.CSS_SELECTOR, 'div[class*=new-item-list-btn]').click()

        wvs(driver, 'LINK_TEXT', 'Перейти в корзину').click()
        time.sleep(3)

        res = None
        for i in wavs(driver, 'CSS', 'tr[class*=ecommerce-tracked-cart-item]'):
            if goods_name in i.text:
                res = True
                message = 'Тест корзины выполнен успешно\n'
                break

        assert res, 'Тест корзины ПРОВАЛЕН'

    except Exception as ex:
        message = 'Тест авторизации: ' + ex.__str__()
        raise ex

    finally:
        with open('shop/tests/logs/' + f'{str(datetime.now())[:-12]}XX_log.txt', 'a') as file:
            file.write(f'{message}')
        driver.close()
        driver.quit()
        time.sleep(2)
