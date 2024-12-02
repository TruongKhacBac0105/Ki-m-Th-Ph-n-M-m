import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestTestsearchtheogiacao():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_testsearchtheogiacao(self):
        self.driver.get("https://cellphones.com.vn/")
        self.driver.set_window_size(1050, 840)

        # Chờ trường tìm kiếm xuất hiện và nhấp vào
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "inp$earch"))
        )
        search_input.click()

        # Nhập từ khóa tìm kiếm
        search_input.send_keys("iphone 16")

        # Chờ biểu tượng tìm kiếm có thể nhấp và nhấp vào
        search_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".svg-inline--fa"))
        )
        search_icon.click()

        # Chờ các tùy chọn sắp xếp có thể nhấp và nhấp vào tùy chọn thứ 2
        sort_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-sort-item:nth-child(2)"))
        )
        sort_option.click()

        # đợi 5 giây
        time.sleep(5)
      
