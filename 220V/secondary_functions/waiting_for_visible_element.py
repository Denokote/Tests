from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_vs(driver, u_type,  selector):
    if u_type == 'CSS':
        return WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    elif u_type == 'ID':
        return WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, selector)))
