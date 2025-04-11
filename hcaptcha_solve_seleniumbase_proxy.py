"""
Example of solving hCaptcha on https://democaptcha.com/demo-form-eng/hcaptcha.html
using:
- SolveCaptcha Python SDK (with or without proxy)
- SeleniumBase (proxy supported, headless off by default)

Steps:
1. Initialize SolveCaptcha SDK.
2. Get the solution token.
3. Launch browser with SeleniumBase.
4. Insert token into h-captcha-response field.
5. Click Submit.
6. Print token and check result.
"""

import os
from dotenv import load_dotenv
from solvecaptcha import Solvecaptcha
from seleniumbase import Driver

# === Load .env variables ===
load_dotenv()

# === API and page config ===
API_KEY = os.getenv("API_KEY")
SITEKEY = "338af34c-7bcb-4c7c-900b-acbec73d7d43"
PAGE_URL = "https://democaptcha.com/demo-form-eng/hcaptcha.html"
HEADLESS = False
USE_PROXY = os.getenv("USE_PROXY", "False").lower() == "true"
CAPTCHA_TIMEOUT = 300  # timeout in seconds

# === Proxy config ===
PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")
PROXY_USER = os.getenv("PROXY_USER")
PROXY_PASS = os.getenv("PROXY_PASS")

def get_proxy_str():
    """
    Format proxy string: username:password@host:port
    """
    return f"{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"

def solve_hcaptcha():
    """
    Solve hCaptcha using SolveCaptcha SDK.
    """
    print("Step 1️⃣  : Initializing SolveCaptcha SDK{}...".format(" with proxy" if USE_PROXY else " without proxy"))
    solver = Solvecaptcha(API_KEY)

    if USE_PROXY:
        proxy_str = get_proxy_str()
        print(f"   ↳ Using proxy: {proxy_str}")
        proxy = {
            "uri": proxy_str,
            "type": "HTTP"
        }
        result = solver.hcaptcha(SITEKEY, PAGE_URL, proxy=proxy, timeout=CAPTCHA_TIMEOUT)
    else:
        result = solver.hcaptcha(SITEKEY, PAGE_URL, timeout=CAPTCHA_TIMEOUT)

    token = result['code']
    print("Step 2️⃣  : Captcha solved! Token:", token)
    return token

def run_browser_with_token(token):
    """
    Open browser, fill token, submit form.
    """
    print("Step 3️⃣  : Launching browser (SeleniumBase){}...".format(" with proxy" if USE_PROXY else " without proxy"))

    driver = Driver(browser="chrome")

    try:
        driver.open(PAGE_URL)
        driver.sleep(5)

        print("Step 4️⃣  : Inserting token into h-captcha-response...")
        driver.execute_script(
            f'document.querySelector("textarea[name=h-captcha-response]").value = "{token}";'
        )
        driver.execute_script(
            f'window.hcaptchaToken = "{token}";'
        )

        print("Step 5️⃣  : Waiting for Submit button and clicking...")
        driver.wait_for_element_visible('input[type="submit"]', timeout=15)
        driver.click('input[type="submit"]')
        driver.sleep(3)

        if driver.is_element_visible('h2') and "Thank you, your message" in driver.get_text('h2'):
            print("Step 6️⃣  : Captcha solved, form submitted!")
        else:
            print("Step 6️⃣  : Token inserted, but success message not found. Check if form was submitted.")
    finally:
        driver.quit()

if __name__ == "__main__":
    token = solve_hcaptcha()
    run_browser_with_token(token)
