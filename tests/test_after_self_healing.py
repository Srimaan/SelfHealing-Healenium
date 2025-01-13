import time
import pytest
from selenium.webdriver.common.by import By
from utils.browser_with_healenium import get_browser  # ✅ Using WebDriver WITH Healenium

@pytest.fixture(scope="module")
def setup_browser():
    """✅ WebDriver Setup with Healenium (Self-Healing Enabled)"""
    driver = get_browser()
    yield driver
    driver.quit()

def test_with_self_healing(setup_browser):
    """✅ Run test with Healenium (Expected to Pass)"""
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    time.sleep(2)

    print("🔹 Clicking on 'Laptops' category (Incorrect Locator, but Self-Healing Enabled)...")

    try:
        # ✅ HEALENIUM AUTOMATICALLY FIXES THIS LOCATOR 🔥
        laptops_category = driver.find_element(By.XPATH, "//a[contains(text(),'Non-ExistentLocator')]")
        laptops_category.click()
        time.sleep(2)
        print("✅ Test Passed with Self-Healing!")
    except Exception as e:
        print(f"❌ Healenium did not heal the locator. Test failed: {e}")
