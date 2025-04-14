
![hcaptcha-solver](https://github.com/user-attachments/assets/9b1e69f4-698c-4aff-af7f-9bb0d5ab50b3)

![Python](https://img.shields.io/badge/python-3.8+-blue)
![SeleniumBase](https://img.shields.io/badge/seleniumbase-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

# Python hCaptcha Solver: Bypass hCaptcha with Proxy using Selenium and SolveCaptcha SDK

This example demonstrates how to solve hCaptcha step-by-step, from start to finish, using the [SolveCaptcha](https://solvecaptcha.com/) [**Python SDK**](https://github.com/solvercaptcha/solvecaptcha-python).
It also shows how to configure and use proxy servers for solving captchas.

This repository contains an example of bypassing hCaptcha using the SolveCaptcha Python SDK and SeleniumBase.
  
## Overview

This repository includes a single script:
- **hcaptcha_solve_seleniumbase_proxy.py** — an end-to-end example that:
  - Uses the SolveCaptcha API to solve hCaptcha on [democaptcha.com](https://democaptcha.com/demo-form-eng/hcaptcha.html).
  - Optionally supports proxy configuration via `.env` file.
  - Controls a Chrome browser using SeleniumBase.
  - Inserts the hCaptcha token and submits the form.
 
## Demonstration (GIF)
![hcaptcha solver demonstration](https://github.com/user-attachments/assets/d1f3ba74-5b7e-4da6-a511-2e2ac8f6ced6)

> ⚠️ This recording is shown at an accelerated speed for demonstration purposes.  In real usage the captcha-solving process takes longer, so please wait while the service returns a result.


## Requirements

- Python 3.x
- [SeleniumBase](https://github.com/seleniumbase/SeleniumBase)
- [SolveCaptcha Python SDK](https://github.com/solvercaptcha/solvecaptcha-python)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for `.env` loading)

> ⚠️ The SolveCaptcha SDK is not published to PyPI. Install it directly from GitHub.

## Installation

```bash
pip install seleniumbase python-dotenv git+https://github.com/solvercaptcha/solvecaptcha-python.git
```

## Configuration

Create a `.env` file in the root directory with the following content:

```env
API_KEY=YOUR_API_KEY
USE_PROXY=False
PROXY_HOST=host
PROXY_PORT=port
PROXY_USER=username
PROXY_PASS=password
```

## Usage

Run the script:
```bash
python hcaptcha_solve_seleniumbase_proxy.py
```

Console output will guide you through the steps:
1. Initialize SDK.
2. Solve the captcha.
3. Launch browser.
4. Insert token.
5. Click submit.
6. Check for success message.

## Adapting captcha bypass for Your Own Website

To use this example on your own site, you'll need to update the captcha configuration:

```python
SITEKEY = "your-site-key"
PAGE_URL = "https://your-site.com/page-with-hcaptcha"
```

Also, be sure to specify your SolveCaptcha API key in the `.env` file:

```env
API_KEY=YOUR_API_KEY
```

⚠️ **Important:**

- The way the captcha token is applied to the page may differ depending on how hCaptcha is implemented on your website.
- Update the JavaScript execution logic if necessary to match your site's requirements.
- Finally, review or adjust any browser actions after token insertion — such as button clicks, custom validations, or post-submit checks — so they reflect the actual behavior of your form.

---

## Notes

- Browser runs in **non-headless** mode by default.
- Proxy usage is optional and controlled via `.env`.
- Target page: https://democaptcha.com/demo-form-eng/hcaptcha.html

## Disclaimer

This project is provided for **demonstration and testing purposes only**. It is not intended to encourage or promote the circumvention of captcha systems on websites without proper authorization.

Captcha systems are often used to protect websites from abuse, and bypassing them may be against the **terms of service** of the target website, and/or **local laws or regulations** in your region.

Before using this code on any third-party site, **you must ensure** that your actions are compliant with the site's rules and applicable legal requirements.

You are solely responsible for how you use this code.

## FAQ

We have also compiled the most common issues encountered when solving hCaptcha into a separate document,  [FAQ.md](./FAQ.md). In it, you will find answers to frequently asked questions.

---

## License

[MIT License](./LICENSE).
