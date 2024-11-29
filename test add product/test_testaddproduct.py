
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestaddproduct():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testaddproduct(self):
    self.driver.get("https://shopee.vn/")
    self.driver.set_window_size(974, 1032)
    self.driver.execute_script("window.scrollTo(0,1100)")
    self.driver.execute_script("window.scrollTo(0,1671)")
    self.driver.find_element(By.CSS_SELECTOR, ".oMSmr0:nth-child(3) .mb-1").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,200)")
    self.driver.find_element(By.CSS_SELECTOR, ".a_JvBi").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar__link-icon").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.LINK_TEXT, "[NHẬP MÃ XM500 GIẢM 500K] Điện thoại thông minh Xiaomi 14T Pro (12+512GB) | Light Fusion 900 | MD 9300+ | Pin 5000mAh").click()
    self.driver.execute_script("window.scrollTo(0,143)")
    self.driver.find_element(By.CSS_SELECTOR, ".suQW3X:nth-child(1) > .shopee-svg-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".suQW3X:nth-child(1) > .shopee-svg-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cart-page-logo")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".AuhAvM:nth-child(3) .aGq8SN:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".icon-shopee-logo").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".header-with-search__logo-wrapper")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
