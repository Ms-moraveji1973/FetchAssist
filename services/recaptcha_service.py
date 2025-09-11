from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def recaptcha(url:str,website_key: str):
    if not url and not website_key:
        raise ValueError("url or website_key is required")
    try :
        print(" We're trying to solve the recaptcha challenge ")
        # install chrome driver for communicate with selenium
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # connect our driver to solve captcha
        solver = RecaptchaSolver(driver=driver)
        driver.get(url)
        # find reCAPTCHA in website
        recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        solver.click_recaptcha_v2(iframe=recaptcha_iframe)
        print('Congratulations....!!!,CAPTCHA solved')
        # get token-captcha from g-recaptcha-response
        g_response_element = driver.find_element(By.ID, "g-recaptcha-response")
        g_response = ""
        while len(g_response) < 100 :
            g_response += g_response_element.get_attribute("value")
            time.sleep(0.5)
        driver.quit()
        print("The Token recaptcha response is found")
        return g_response

    except Exception as e:
        print(f'Something went wrong : {e}')
        driver.quit()
        print('Driver was quit')
        raise ValueError(f'Something went wrong : {e}')
