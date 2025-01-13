from selenium import webdriver

def get_browser():
    """✅ WebDriver Setup with Healenium (Self-Healing Enabled)"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-proxy-server")

    # ✅ CONNECTING TO HEALENIUM PROXY (Self-Healing Enabled)
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",  # 🔥 HEALENIUM PROXY 🔥
        options=options
    )
    return driver
