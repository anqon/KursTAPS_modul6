import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests.helpers.support_functions import *
from Tests.page_objects import iframe
from time import  sleep
from selenium.webdriver.common.keys import Keys


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.url ='http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test1_click_iframe(self):
        iframe.click_iframe_tag(self.driver)
        self.assertTrue(iframe.iframe_content_visibility(self.driver))

    def test2_iframe_click_first_button(self):
        iframe.click_iframe_tag(self.driver)
        self.assertTrue(iframe.click_inside_iframe(self.driver))
        iframe.make_screen(self.driver)
