from selenium import webdriver
from shop.data.data import user_agent


def start():
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(executable_path='/chromedriver/chromedriver_linux64.zip',
                              options=options)

    return driver
