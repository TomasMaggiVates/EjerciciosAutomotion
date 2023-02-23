# Open browser
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
password_locator.send_keys('Password123')

# Push Submit button
button_locator = driver.find_element(By.ID, 'submit')
button_locator.click()

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
url = driver.current_url
assert url.__contains__('practicetestautomation.com/logged-in-successfully/')

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
expected = ['Congratulations', 'successfully logged in']
texts = driver.find_elements(By.TAG_NAME, 'strong')[0].text.split('.')

# compare every text with a expected prase
for text, k in zip(texts, expected):
    assert text.__contains__(k)

# Verify button Log out is displayed on the new page
logout_button = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')
assert logout_button
