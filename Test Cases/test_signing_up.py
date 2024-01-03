import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Suite 1 - Signing Up
We are performing functionality tests, in this script we are testing the cases:
    - 1.1 > Sign Up with Hotmail mail
    - 1.2 > Sign Up with Outlook mail
    - 1.3 > Sign Up with Walla mail
    - 1.4 > Sign up with 8 characters in the password
    - 1.5 > Sign up with 9 characters in the password
"""
users_list1 = [['tt0@htomail.com', '123456A'], ['a1aatt200@outlook.com', '123456A'], ['a1ttaa300@walla.com', '123456A'], ['aadcsttttdvc12@gmail.com', '1234567A'], ['aadcsdvttttttc12@gmail.com', '12345678A']]


@pytest.mark.parametrize("list_of_users", users_list1)
def test_signing_up(list_of_users):
    driver = webdriver.Chrome()
    # Step 1 - Open SVBurger on Chrome
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Step 2 - Click on the "Sign Up" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button').click()
    # Step 3 - Fill the first name textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]').send_keys('aaaaaa')
    # Step 4 - Fill the last name textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[2]').send_keys('aaaaaa')
    # Step 5 - Fill the email textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]').send_keys(list_of_users[0])
    # Step 6 -Fill the new password textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]').send_keys(list_of_users[1])
    # Step 7 - Fill the confirmation password textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]').send_keys(list_of_users[1])
    # Step 8 - Click on the "Sign Up" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button').click()
    # If we successfully sign up we can know if the "Log Out" button below is displayed
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]').is_displayed()


"""
Suite 1 - Signing Up
We are performing error handling tests, in this script we are testing the cases:
    - 1.6 > Sign Up without filling the first name
    - 1.7 > Sign Up without filling the last name
"""
users_list2 = [['', 'aaaaaa', 'txxt0@htomail.com', 'First name must be in English letters only'], ['aaaaaa', '', 'a1axxxatt200@outlook.com', 'Last name must be in English letters only']]


@pytest.mark.parametrize("list_of_users", users_list2)
def test_signing_up_without_first_name(list_of_users):
    driver = webdriver.Chrome()
    # Step 1 - Open SVBurger on Chrome
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Step 2 - Click on the "Sign Up" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button').click()
    # Step 3 - Fill the first name textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]').send_keys(list_of_users[0])
    # Step 4 - Fill the last name textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[2]').send_keys(list_of_users[1])
    # Step 5 - Fill the email textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]').send_keys(list_of_users[2])
    # Step 6 -Fill the new password textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]').send_keys('123456A')
    # Step 7 - Fill the confirmation password textbox
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]').send_keys('123456A')
    # Step 8 - Click on the "Sign Up" button
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button').click()
    # We should get an error modal, this error modal should have and error message which we need to check if it equals the error message that we should get for each error
    time.sleep(20)
    my_alert = driver.switch_to.alert
    assert my_alert.text == list_of_users[3]