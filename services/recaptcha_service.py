from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def recaptcha(url:str):
    if not url:
        raise ValueError("url or website_key is required")
    try :
        print(" We're trying to solve the recaptcha challenge ")
        # install chrome driver for communicate with selenium
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # connect our driver to solve captcha
        solver = RecaptchaSolver(driver=driver)
        driver.get(url)
        # wait to get from reCAPTCHA
        element = WebDriverWait(driver , 20).until(
            EC.presence_of_element_located((By.XPATH,'//iframe[@title="reCAPTCHA"]'))
        )
        print('find element')
        solver.click_recaptcha_v2(iframe=element)
        print('Congratulations....!!!,CAPTCHA solved')
        # wait to get token-captcha from g-recaptcha-response
        g_element = WebDriverWait(driver , 20).until(
            EC.presence_of_element_located((By.ID,"g-recaptcha-response"))
        )
        g_response = ""
        while len(g_response) < 100 :
            g_response += g_element.get_attribute("value")
            time.sleep(0.5)
        driver.quit()
        print("The Token recaptcha response is found")
        return g_response

    except Exception as e:
        print(f'Something went wrong : {e}')
        driver.quit()
        print('Driver was quit')
        raise ValueError(f'Something went wrong : {e}')
