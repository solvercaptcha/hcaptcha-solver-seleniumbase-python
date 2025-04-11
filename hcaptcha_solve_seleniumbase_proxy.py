"""
Example of solving hCaptcha on https://democaptcha.com/demo-form-eng/hcaptcha.html
using:
- SolveCaptcha Python SDK (with or without proxy)
- SeleniumBase (proxy supported, headless off by default)
"""

import os
from dotenv import load_dotenv
from solvecaptcha import Solvecaptcha
from seleniumbase import Driver
from utilities.print_project_info import print_project_info

# ── Coloured console output ────────────────────────────────────────────────────
from colorama import Fore, Style, init

init(autoreset=True)  # reset style after each line


def log(level: str, message: str) -> None:
    """Print a colour‑coded log message."""
    colours = {
        "INFO": Fore.CYAN,
        "SUCCESS": Fore.GREEN,
        "WARN": Fore.YELLOW,
        "ERROR": Fore.RED,
    }
    colour = colours.get(level.upper(), Fore.WHITE)
    print(f"{colour}{level:<8}{Style.RESET_ALL} {message}")


# ── Load .env variables ────────────────────────────────────────────────────────
load_dotenv()

# ── API and page config ────────────────────────────────────────────────────────
API_KEY = os.getenv("API_KEY")
SITEKEY = "338af34c-7bcb-4c7c-900b-acbec73d7d43"
PAGE_URL = "https://democaptcha.com/demo-form-eng/hcaptcha.html"
HEADLESS = False
USE_PROXY = os.getenv("USE_PROXY", "False").lower() == "true"
CAPTCHA_TIMEOUT = 300  # seconds

# ── Proxy config ───────────────────────────────────────────────────────────────
PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")
PROXY_USER = os.getenv("PROXY_USER")
PROXY_PASS = os.getenv("PROXY_PASS")


def get_proxy_str() -> str:
    """Return proxy in the format username:password@host:port."""
    return f"{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"


def solve_hcaptcha() -> str:
    """Solve hCaptcha via SolveCaptcha SDK and return the solution token."""
    log("INFO", f"Initialising SolveCaptcha SDK ({'with proxy' if USE_PROXY else 'without proxy'})")
    solver = Solvecaptcha(API_KEY)

    if USE_PROXY:
        proxy = {"uri": get_proxy_str(), "type": "HTTP"}
        log("INFO", f"Using proxy: {proxy['uri']}")
        result = solver.hcaptcha(SITEKEY, PAGE_URL, proxy=proxy, timeout=CAPTCHA_TIMEOUT)
    else:
        result = solver.hcaptcha(SITEKEY, PAGE_URL, timeout=CAPTCHA_TIMEOUT)

    token = result["code"]
    log("SUCCESS", "Captcha solved")
    return token


def run_browser_with_token(token: str) -> None:
    """Open browser, inject token, submit form, verify result."""
    log("INFO", f"Launching SeleniumBase browser ({'with proxy' if USE_PROXY else 'without proxy'})")
    driver = Driver(browser="chrome", headless=HEADLESS)

    try:
        driver.open(PAGE_URL)
        driver.sleep(5)

        log("INFO", "Injecting token into h-captcha-response")
        driver.execute_script(
            'document.querySelector("textarea[name=h-captcha-response]").value = arguments[0];',
            token,
        )
        driver.execute_script("window.hcaptchaToken = arguments[0];", token)

        log("INFO", "Clicking Submit button")
        driver.wait_for_element_visible('input[type="submit"]', timeout=15)
        driver.click('input[type="submit"]')
        driver.sleep(3)

        if driver.is_element_visible("h2") and "Thank you, your message" in driver.get_text("h2"):
            log("SUCCESS", "Form submitted successfully")
        else:
            log("WARN", "Token injected, but success message not found — verify submission manually")
    finally:
        driver.quit()


if __name__ == "__main__":
    print_project_info()
    try:
        solution_token = solve_hcaptcha()
        run_browser_with_token(solution_token)
    except Exception as exc:
        log("ERROR", str(exc))
        raise
