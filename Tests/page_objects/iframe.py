from Tests.helpers.support_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime


iframe_tab = "iframe-header"
iframe_content = "iframe-content"
iframe_main = "iframe"
button1 = "simpleButton1"
message = "whichButtonIsClickedMessage"

def click_iframe_tag(driver_instance):
    elem = driver_instance.find_element(By.ID, iframe_tab)
    elem.click()


def iframe_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, iframe_content)
    return elem.is_displayed()


def click_inside_iframe(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, iframe_main, time_to_wait=5)
    driver_instance.switch_to.frame(driver_instance.find_element(By.TAG_NAME,'iframe'))
    driver_instance.find_element(By.ID, button1).click()
    output = driver_instance.find_element(By.ID, message).text
    if output == 'Button 1 was clicked!':
        return True
    else:
        return False


def make_screen(driver_instance):
    elem = driver_instance.find_element(By.ID, "whichButtonIsClickedMessage")
    driver_instance.execute_script("arguments[0].scrollIntoView();", elem)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver_instance.save_screenshot(r'C:\Users\ziele\PycharmProjects\KursTAPS_modul6\Tests\screenshots\iframe'+now+'.png')

