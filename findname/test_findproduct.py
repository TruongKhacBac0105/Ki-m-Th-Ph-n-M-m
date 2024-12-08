import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://www.lazada.vn/#?")
        self.driver.set_window_size(1936, 1048)
        self.driver.find_element(By.ID, "q").click()
        self.driver.find_element(By.ID, "q").send_keys("iphone 15 pro max")
        self.driver.find_element(By.LINK_TEXT, "SEARCH").click()

        # Chờ và xử lý captcha nếu cần
        try:
            captcha_frame = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='captcha']"))
            )
            print("Captcha xuất hiện, hãy xử lý thủ công.")
            self.driver.switch_to.frame(captcha_frame)
            input("Nhấn Enter sau khi captcha đã được xác minh...")
            self.driver.switch_to.default_content()
        except:
            print("Không phát hiện captcha.")

        self.driver.find_element(By.LINK_TEXT, "(Siêu Tiệc Giáng Sinh 06-08.12) iPhone 15 Pro Max - Hàng Chính Hãng VN/A").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pdp-mod-product-badge-title").click()
        element = self.driver.find_element(By.ID, "block-BDipfo2QZad")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        assert self.driver.find_element(By.CSS_SELECTOR, ".pdp-mod-product-badge-title").text == "(Siêu Tiệc Giáng Sinh 06-08.12) iPhone 15 Pro Max - Hàng Chính Hãng VN/A"