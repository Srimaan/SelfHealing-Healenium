import time
import pytest
from selenium.webdriver.common.by import By
from utils.browser_without_healenium import get_browser  # ❌ Using WebDriver WITHOUT Healenium

@pytest.fixture(scope="module")
def setup_browser():
    """🚫 Standard Selenium WebDriver (No Self-Healing)"""
    driver = get_browser()
    yield driver
    driver.quit()

def test_without_self_healing(setup_browser):
    """🚫 Run test without self-healing (Expected to Fail)"""
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    time.sleep(2)

    print("🔹 Clicking on 'Laptops' category (Incorrect Locator)...")

    # ❌ This will fail because locator is incorrect
    laptops_category = driver.find_element(By.XPATH, "//a[contains(text(),'Non-ExistentLocator')]")
    laptops_category.click()

    print("✅ Test Passed (Unexpected)")  # This should never execute if the test fails correctly
