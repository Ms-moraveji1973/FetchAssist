# 🧩 CAPTCHA Solver (Practice Project)

This project is a simple toolkit and API for learning and practicing techniques to bypass web security challenges such as reCAPTCHA and Cloudflare. The main goal is to gain hands-on experience with libraries like `cloudscraper`, `selenium`, and `pytesseract`. It is **not** intended to be a 100% reliable or production-ready solution.

---
Note: Only the frontend (HTML and visual design) of this project was generated using AI.
## Features

* **Bypass Cloudflare Challenges:** Uses `cloudscraper` to get around some basic Cloudflare protections.
* **Solve reCAPTCHA v2 with Selenium:** Includes a prototype for interacting with Google reCAPTCHA via `selenium_recaptcha_solver`.
* **Simple Image CAPTCHA Solver:** Contains a custom algorithm for solving simple image-based CAPTCHAs with specific patterns (50–60% accuracy).
* **Analytics Dashboard:** A simple dashboard (`recaptcha_dashboard`) to view history and details of reCAPTCHA v2 solving attempts.
* **FastAPI-based API:** Provides endpoints for easy integration with other apps and scripts.
* **Extensible:** Project structure allows you to easily add new algorithms and methods.

---

##  Challenges & Key Notes

* **Educational Purpose Only:** This project is created solely for learning and training. Modern CAPTCHA systems (like reCAPTCHA v3 and hCaptcha) are much more advanced, and bypassing them is not guaranteed with these tools.
* **Limited Accuracy**: The image CAPTCHA solver is tailored for a specific pattern and does not achieve high accuracy. It’s meant to demonstrate image processing and pytesseract usage. For testing this solver, you can use the sample CAPTCHA page at https://firatozz.github.io/repo-pages/simpleCaptcha.html — this page uses the same (or very similar) CAPTCHA pattern that the example solver was designed for.
* **Instability:** Websites frequently update their security systems. The code may stop working over time and require updates.
* **Third-party Dependencies:** Functionality relies on external libraries and tools that may change in the future.

---

## Requirements

* Python 3.9+

---

## Installation & Setup

1. Clone the repository and create a virtual environment:

```bash
git clone <FetchAssist>
cd <FetchAssist>
python -m venv venv
```

2. Activate the virtual environment and install dependencies:

```bash
source venv/bin/activate

pip install -r requirements.txt
```

---

## Running the API

To start the FastAPI server, run:

```bash
fastapi dev main.py
```

---

## reCAPTCHA Dashboard :
```
Open recaptcha_dashboard.html 
```

author: muhammad1973
