import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


"""
Suite 3 - ordering
We are performing functionality tests, in this script we are testing the cases:
    - 3.1 > Ordering the 2 meals “Combo Meal” & “Kids Meal”
    - 3.2 > Ordering the 2 meals “Combo Meal” & “Burger”
    - 3.3 > Ordering the 2 meals “Combo Meal” & “Vegan”
    - 3.4 > Ordering the 2 meals “Combo Meal” & “Sides”
"""
products_list = [['//*[@id="root"]/div[2]/div[1]/div/div/div/div[2]/div/div', '107.8$'], ['//*[@id="root"]/div[2]/div[1]/div/div/div/div[3]/div/div', '114.4$'], ['//*[@id="root"]/div[2]/div[1]/div/div/div/div[4]/div/div', '114.4$'], ['//*[@id="root"]/div[2]/div[1]/div/div/div/div[5]/div/div', '78.1$']]


@pytest.mark.parametrize("list_of_products", products_list)
def test_ordering_two_meals(list_of_products):
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
    # Step 7 - Click on the second meal
    driver.find_element(By.XPATH, list_of_products[0]).click()
    # Step 8 - Click on the "Reserve" button after it changes to clickable
    # Waiting until the button changes to clickable
    reserve_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')))
    driver.execute_script("arguments[0].click();", reserve_btn)
    # Step 9 - Click on the "Send" button
    send_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div[1]/button')))
    driver.execute_script("arguments[0].click();", send_btn)
    # Test if the SVBurger Summary modal opens and shows the total price for the order
    time.sleep(5)
    total_price_string = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]')))
    total_price = total_price_string.text.split(' ')
    print(total_price[1])
    assert total_price[1] == list_of_products[1]


"""
Suite 3 - ordering
We are performing functionality test, in this script we are testing the case:
    - 3.5 > Unselecting a selected meal
"""


def test_unselecting_selected_meal():
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
    # Step 6 - Click on the "Combo Meal" to select it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div').click()
    # Step 7 - Click on the "Combo Meal" to unselect it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div').click()
    # We need to test if the meal card has the white background in the style attribute to make sure it was unselected
    meal_card_style_attribute = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div').get_attribute("style")
    assert meal_card_style_attribute.__contains__('background-color: white')


"""
Suite 3 - ordering
We are performing error handling tests, in this script we are testing the case:
    - 3.6 > Selecting 4 meal cards
"""


def test_selecting_four_meals():
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
    # Step 6 - Click on the "Combo Meal" to select it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div').click()
    # Step 7 - Click on the "Kids Meal" to select it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[2]/div/div').click()
    # Step 8 - Click on the "Burger" meal to select it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[3]/div/div').click()
    # Step 9 - Click on the "Vegan" meal to select it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[4]/div/div').click()
    time.sleep(5)
    # We need to test if the "Vegan" meal card has the white background in the style attribute to make sure it was unselected
    meal_card_style_attribute = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div/div[4]/div').get_attribute("style")
    print(meal_card_style_attribute)
    assert meal_card_style_attribute.__contains__('background-color: white')


"""
Suite 3 - ordering
We are performing error handling tests, in this script we are testing the case:
    - 3.7 > Selecting more than 2 meals in the meal quantity
"""


def test_selecting_more_than_two_in_the_meal_quantity():
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
    # Step 6 - Click on the "Combo Meal" to select it
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div').click()
    # Step 7 - Click on the "Reserve" button after it changes to clickable
    # Waiting until the button changes to clickable
    reserve_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')))
    driver.execute_script("arguments[0].click();", reserve_btn)
    # Step 8 - Fill the value 3 in the meal quantity
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input').send_keys('3')
    # Testing if the order summary modal appears after clicking the "Send" button, the modal should not appear if we select more than 2 meal quantity
    send_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/button')))
    driver.execute_script("arguments[0].click();", send_btn)
    time.sleep(5)
    assert not driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]').is_displayed()
