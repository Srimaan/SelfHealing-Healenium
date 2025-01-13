from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_browser():
    """🚫 Standard Selenium WebDriver (No Self-Healing)"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-proxy-server")

    # ❌ Running WebDriver without Healenium (Locator will fail)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
