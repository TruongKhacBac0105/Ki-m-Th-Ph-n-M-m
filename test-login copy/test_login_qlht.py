import pytest
import time
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginQlht:
  
    def setup_method(self, method):
        load_dotenv()

        self.username = os.getenv('LOGIN_USERNAME')  
        self.password = os.getenv('LOGIN_PASSWORD')
    
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_loginqlht(self):
        self.driver.get("https://qlht.ued.udn.vn/sinhvien")
        self.driver.set_window_size(1920, 1080)

        time.sleep(2)

        self.driver.find_element(By.ID, "txt_Login_ten_dang_nhap").send_keys(self.username) # thay đổi số sinh viên
        self.driver.find_element(By.ID, "pw_Login_mat_khau").send_keys("wrongpassword")
        self.driver.find_element(By.NAME, "bt_Login_submit").click()
        
        time.sleep(1)

        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#error_box > div:nth-child(2)"))
            )
            if error_message.text == "Mã đăng nhập hoặc mật khẩu không đúng":
                print("Thông báo lỗi: Mã đăng nhập hoặc mật khẩu không đúng. Đang thử lại với thông tin chính xác.")
            else:
                print("Lỗi không xác định, nhưng tiếp tục đăng nhập lại.")
            
        except Exception as e:
            print(f"Không tìm thấy thông báo lỗi. Tiếp tục thử đăng nhập lại. Lỗi: {str(e)}")
        
        self.driver.find_element(By.ID, "txt_Login_ten_dang_nhap").clear()
        self.driver.find_element(By.ID, "txt_Login_ten_dang_nhap").send_keys(self.username)# thay đổi số sinh viên
        self.driver.find_element(By.ID, "pw_Login_mat_khau").clear()
        self.driver.find_element(By.ID, "pw_Login_mat_khau").send_keys(self.password)# thay đổi mk
        self.driver.find_element(By.NAME, "bt_Login_submit").click()

        time.sleep(1)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "thoikhoabieu"))
            )

            self.driver.find_element(By.ID, "thoikhoabieu").click()
            time.sleep(1)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "cmb_sr_ds_hoc_ky"))
            )

            self.driver.find_element(By.ID, "cmb_sr_ds_hoc_ky").click()
            dropdown = self.driver.find_element(By.ID, "cmb_sr_ds_hoc_ky")

            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

            options = dropdown.find_elements(By.TAG_NAME, "option")
            for option in options:
                if option.text == '1': 
                    option.click()
                    break

            selected_option = dropdown.find_element(By.XPATH, "//option[. = '1']")
            assert selected_option.is_selected(), "Option '1' không được chọn đúng cách."

            
            self.driver.find_element(By.ID, "cmbkieuin").click()
            time.sleep(1)

            dropdown = self.driver.find_element(By.ID, "cmbkieuin")
            dropdown.find_element(By.XPATH, "//option[. = 'Tách trang theo tuần']").click()
            time.sleep(1)

            self.driver.find_element(By.ID, "cmbtuan").click()
            time.sleep(1)

            dropdown = self.driver.find_element(By.ID, "cmbtuan")
            dropdown.find_element(By.XPATH, "//option[. = 'Tuần 10 (03-03-2025 đến 09-03-2025)']").click()
            time.sleep(1)

            self.driver.find_element(By.ID, "cmb_s_sr").click()
            time.sleep(1)
            
            self.driver.find_element(By.CSS_SELECTOR, "#tb_main_Array_9_body .body:nth-child(8) > td:nth-child(2)").click()

            text_from_element = self.driver.find_element(By.CSS_SELECTOR, "#tb_main_Array_9_body .body:nth-child(8) > td:nth-child(2)").text
            assert text_from_element.replace('\n', ' ') == "31231352 - 21-0203 Kiểm thử phần mềm Phòng: A5-304"
            time.sleep(1)

            self.driver.find_element(By.LINK_TEXT, "Thoát").click()
            time.sleep(1)
            assert self.driver.switch_to.alert.text == "Xác nhận thoát khỏi chương trình?"
            self.driver.switch_to.alert.accept()

            print("Test Passed: Đăng nhập thành công và các chức năng hoạt động như mong đợi.")
        except Exception as e:
            pytest.fail(f"Test Failed: {str(e)}")

if __name__ == "__main__":
    pytest.main()
