from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_all_vs(driver, u_type,  selector):
    if u_type == 'CSS':
        return WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
    elif u_type == 'ID':
        return WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located((By.ID, selector)))
    elif u_type == 'LINK_TEXT':
        return WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, selector)))


def wait_vs(driver, u_type,  selector):
    if u_type == 'CSS':
        return WebDriverWait(driver, timeout=20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    elif u_type == 'ID':
        return WebDriverWait(driver, timeout=20).until(EC.visibility_of_element_located((By.ID, selector)))
    elif u_type == 'LINK_TEXT':
        return WebDriverWait(driver, timeout=20).until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))
