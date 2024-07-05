from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

class Pagebase:
    def __init__(self,driver):
        self.driver = driver
    def wait_element_visibility_of(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.visibility_of_element_located(locator))
        return element
    def wait_element_visibility_of_all(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.visibility_of_all_elements_located(locator))
        return element
    def wait_element_of_be_clikcable(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.element_to_be_clickable(locator))
        return element
    def wait_element_of_presence(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.presence_of_element_located(locator))
        return element
    def wait_until_not_visibility_of(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until_not(EC.visibility_of_element_located(locator))
        return element