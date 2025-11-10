from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_user_flow():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed and in your PATH
    driver.get("http://localhost:3000")  # Adjust the URL if necessary

    # Test user registration
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()

    time.sleep(2)  # Wait for the registration to complete

    # Test user login
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()

    time.sleep(2)  # Wait for the login to complete

    # Test adding a transaction
    driver.find_element(By.LINK_TEXT, "Add Transaction").click()
    driver.find_element(By.NAME, "amount").send_keys("10000")
    driver.find_element(By.NAME, "category").send_keys("Food")
    driver.find_element(By.NAME, "date").send_keys("2023-10-01")
    driver.find_element(By.NAME, "submit").click()

    time.sleep(2)  # Wait for the transaction to be added

    # Test viewing transactions
    driver.find_element(By.LINK_TEXT, "Transactions").click()
    assert "Food" in driver.page_source  # Check if the transaction appears in the list

    # Test setting a savings goal
    driver.find_element(By.LINK_TEXT, "Savings Goals").click()
    driver.find_element(By.NAME, "goalName").send_keys("Emergency Fund")
    driver.find_element(By.NAME, "goalAmount").send_keys("50000")
    driver.find_element(By.NAME, "submit").click()

    time.sleep(2)  # Wait for the goal to be set

    # Verify the goal is set
    assert "Emergency Fund" in driver.page_source

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_user_flow()