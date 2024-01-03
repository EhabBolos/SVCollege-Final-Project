import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Suite 2 - Signing In
We are performing functionality tests, in this script we are testing the cases:
    - 2.1 > Sign In with Hotmail mail
    - 2.2 > Sign In with Outlook mail
    - 2.3 > Sign In with Walla mail
    - 2.4 > Sign In with 8 characters in the password
    - 2.5 > Sign In with 9 characters in the password
"""
users_list3 = [['tt0@htomail.com', '123456A'], ['a1aatt200@outlook.com', '123456A'], ['a1ttaa300@walla.com', '123456A'], ['aadcsttttdvc12@gmail.com', '1234567A'], ['aadcsdvttttttc12@gmail.com', '12345678A']]


@pytest.mark.parametrize("list_of_users", users_list3)
def test_signing_in(list_of_users):
    driver = webdriver.Chrome()
    # Step 1 - Open SVBurger on Chrome
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Step 2 - Click on the "Sign In" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button').click()
    # Step 3 - Fill the email textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]').send_keys(list_of_users[0])
    # Step 4 - Fill the password textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]').send_keys(list_of_users[1])
    # Step 5 - Click on "Sign in" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button').click()
    # If we successfully signed in we can know if the "Log Out" button below is displayed
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]').is_displayed()


"""
Suite 2 - Signing In
We are performing error handling tests, in this script we are testing the cases:
    - 2.6 > Sign Up without filling the password
    - 2.7 > Sign Up with a wrong password
"""
users_list4 = [['tt0@htomail.com', ''], ['a1aatt200@outlook.com', '00000000a']]


@pytest.mark.parametrize("list_of_users", users_list4)
def test_signing_in(list_of_users):
    driver = webdriver.Chrome()
    # Step 1 - Open SVBurger on Chrome
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Step 2 - Click on the "Sign In" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button').click()
    # Step 3 - Fill the email textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]').send_keys(list_of_users[0])
    # Step 4 - Fill the password textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]').send_keys(list_of_users[1])
    # Step 5 - Click on "Sign in" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button').click()
    # We should get an error modal, this error modal should have an error message which we need to check if it equals the error message that we should get for each error
    time.sleep(20)
    my_alert = driver.switch_to.alert
    error_message = my_alert.text
    my_alert.dismiss()
    assert error_message == 'Failed to log in'