import time
import pytest
from selenium.webdriver.common.by import By


class Test_Negativeusername:

    @pytest.mark.invalid_username
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password,expected_error_message",
                             [
                                 ("incorrectUser", "Password123", "Your username is invalid!"),
                                 ("student", "incorrectPassword", "Your password is invalid!")
                             ])
    def test(self, driver, username, password, expected_error_message) -> None:
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys(password)

        # Push Submit button
        button_locator = driver.find_element(By.ID, 'submit')
        button_locator.click()

        # Verify error message is displayed
        time.sleep(1)
        message = driver.find_element(By.XPATH, '//*[@id="error"]')
        assert message.is_displayed()

        # Verify error message text is "Your username is invalid!"
        error_text = driver.find_element(By.XPATH, '//*[@id="error"]').text
        assert error_text == expected_error_message
