from selenium import webdriver
from test_authorization import test_autorization
from data import user_agent

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(executable_path='/home/denis/study/Andreev/chromedriver/chromedriver_linux64.zip',
                          options=options)

test_autorization(driver)
