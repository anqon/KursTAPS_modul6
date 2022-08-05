from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from datetime import datetime


def wait_for_visibility_of_element (driver_instance, xpath, time_to_wait=5):
    try:
        elem=WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_id (driver_instance, id, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem

def generate_date_now():
    datetime.now().strftime('%Y-%m-%d_%H-%M-%S')