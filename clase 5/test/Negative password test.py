# Open browser
# selenium 4
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_Negativepassword:

    @pytest.mark.invalid_password
    def test(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(3)

        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('student')

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys('incorrectPassword')

        # Push Submit button
        button_locator = driver.find_element(By.ID, 'submit')
        button_locator.click()

        # Verify error message is displayed
        assert driver.find_element(By.XPATH, '//*[@id="error"]').is_displayed()

        # Verify error message text is "Your username is invalid!"
        error_text = driver.find_element(By.XPATH, '//*[@id="error"]').text
        assert error_text == "Your password is invalid!"
