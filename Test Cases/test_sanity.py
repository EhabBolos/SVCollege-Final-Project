from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_sanity():
    driver = webdriver.Chrome()
    # Step 1 - Open SVBurger on Chrome
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # step 2 - Click the "Sign In" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button').click()
    # Step 3 - Enter the email in the email field
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]').send_keys('svburger_web@gmail.com')
    # Step 4 - Enter the password in the password field
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]').send_keys('123456A')
    # Step 5 - Click on the "Sign in" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button').click()
    # Step 6 - Click on the "Combo Meal"
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div').click()
    # Step 7 - Click on the "Reserve" button after it changes to clickable
    # Waiting until the button changes to clickable
    reserve_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')))
    driver.execute_script("arguments[0].click();", reserve_btn)
    # Step 8 - Click on the "Send" button
    send_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/button')))
    driver.execute_script("arguments[0].click();", send_btn)
    # Test if the SVBurger Summary modal opens
    time.sleep(20)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div').is_displayed()
