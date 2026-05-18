import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv("config.env")

CHROME_PATH = "/app/.chrome-for-testing/chrome-linux64/chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "")
MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "")
MEGA_API = os.environ.get("MEGA_API", "")

chrome_options = Options()
chrome_options.binary_location = CHROME_PATH
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-extensions")

service = Service(CHROMEDRIVER_PATH)

def login():
    """Logs in to MEGA and verifies success."""
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get("https://mega.nz/login")
        print("Page Title:", driver.title)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-name3"))
        )
        email_input.send_keys(MEGA_EMAIL)

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-password3"))
        )
        password_input.send_keys(MEGA_PASSWORD)
        password_input.send_keys(Keys.RETURN)

        print("Login attempted...")

        WebDriverWait(driver, 10).until(
            EC.url_contains(f"fm/{MEGA_API}")
        )

        print("✅ Login successful!")

    except Exception as e:
        print(f"❌ Login failed: {e}")

    finally:
        driver.quit()
        print("WebDriver session ended.")

login()

while True:
    print("⏳ Waiting for 30 minutes before re-login...")
    time.sleep(1800)
    login()
