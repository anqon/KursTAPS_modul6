from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

iframe_header = 'iframe-header'
iframe_content = 'iframe-content'
button1 = "simpleButton1"

driver = webdriver.Chrome()
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)
sleep(1)
driver.find_element(By.ID, iframe_header).click()
sleep(3)
elem=driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))
driver.find_element(By.ID, button1).click()
elem.screenshot(r'C:\Users\ziele\PycharmProjects\KursTAPS_modul6\Tests\screenshots\screen5.png')
driver.quit()
