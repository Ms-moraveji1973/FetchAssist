# 🧩 CAPTCHA Solver

This project provides a simple API and tools to **bypass reCAPTCHA** and **Cloudflare-protected websites** using  
[`cloudscraper`](https://github.com/VeNoMouS/cloudscraper) and `selenium_recaptcha_solver`.

---

## Features
- Solve **Cloudflare challenges** with `cloudscraper`  
- Handle **Google reCAPTCHA** using Selenium  
- FastAPI endpoints to integrate with other applications  
- Easy to extend for other scraping or automation tasks  

---

## Requirements
- Python **3.9+**

---

## Installation and Run Project
Clone the repository and install dependencies:

```bash
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

## Run
```bash
fastapi dev main.py
```
