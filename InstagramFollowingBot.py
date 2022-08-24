import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
import time
s = Service("path to chromedriver.exe") #chrome
f = Service("path to geckodriver.exe") #firefox
while 1>0:
    try:
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        allow = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        allow.click()
        time.sleep(2)
        username = driver.find_element(By.NAME, "username")
        username.send_keys("Type_USERNAME")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("Type_PASSWORD")
        log_in = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[3]/button/div")
        time.sleep(1.5)
        log_in.click()
        time.sleep(random.uniform(6,6.5))
        not_now = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
        not_now.click()
        time.sleep(random.uniform(2,2.5))
        not_now_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        not_now_2.click()
        driver.get("https://www.instagram.com/cristiano/")
        time.sleep(random.uniform(5,5.5))
        cristiano_fans = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div")
        cristiano_fans.click()
        time.sleep(random.uniform(2,2.5))
        fans = driver.find_elements(By.CLASS_NAME, ("_acan._acap._acas"))
        a=2
        enabled = True
        while 1>0 and enabled == True:
            time.sleep(random.uniform(1,1.5))
            fans[a].click()
            a += 1
            fans = driver.find_elements(By.CLASS_NAME, ("_acan._acap._acas"))
            print(a)

    except:
        try:
            print("chrome fail")
            driver.close()
            driver_firefox = webdriver.Firefox(service=f)
            b=2
            driver_firefox.get("https://www.instagram.com/")
            time.sleep(2)
            allow = driver_firefox.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
            allow.click()
            time.sleep(2)
            username = driver_firefox.find_element(By.NAME, "username")
            username.send_keys("Type_Username")
            password = driver_firefox.find_element(By.NAME, "password")
            password.send_keys("Type_Password")
            log_in = driver_firefox.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[3]/button/div")
            time.sleep(1.5)
            log_in.click()
            time.sleep(random.uniform(6,6.5))
            not_now = driver_firefox.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
            not_now.click()
            time.sleep(random.uniform(2,2.5))
            not_now_2 = driver_firefox.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            not_now_2.click()
            driver_firefox.get("https://www.instagram.com/cristiano/")
            time.sleep(random.uniform(5,5.5))
            cristiano_fans = driver_firefox.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div")
            cristiano_fans.click()
            time.sleep(random.uniform(2,2.5))
            fans = driver_firefox.find_elements(By.CLASS_NAME, ("_acan._acap._acas"))
            enabled_firefox = True
            while b<100 and enabled_firefox == True:
                time.sleep(random.uniform(1,1.5))
                fans[b].click()
                b += 1
                fans = driver_firefox.find_elements(By.CLASS_NAME, ("_acan._acap._acas"))
                print(b)
        except:
            print("firefox fail")
    finally:
        driver_firefox.close()
        print("standby")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Time: ", current_time)
        time.sleep(240) 

