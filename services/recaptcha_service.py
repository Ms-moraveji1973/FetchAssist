from fastapi import Depends
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy.orm import Session
import time

import models

def recaptcha(db:Session,url:str):
    start_time = time.time()
    if not url:
        raise ValueError("url or website_key is required")
    try :
        start_time = time.time()
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
        duration = time.time() - start_time
        add_query = models.Logs(website_url=url,duration=duration,error_message=None)
        db.add(add_query)
        db.commit()
        print('We commited in database (: ')
        driver.quit()
        print("The Token recaptcha response is found")
        print(f"It took {duration} seconds to solve the recaptcha challenge")
        return g_response

    except Exception as e:
        print(f'Something went wrong : {e}')
        duration = time.time() - start_time
        add_query = models.Logs(website_url=url,duration=duration,error_message=str(e))
        db.add(add_query)
        db.commit()
        driver.quit()
        print('Driver was quit')
        raise ValueError(f'Something went wrong : {e}')




