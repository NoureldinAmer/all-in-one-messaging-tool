import smtplib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.options import Options
import time

def send_to_discord(recepient: str, msg: str) -> bool:
    if recepient == None or msg == "":
        return
    try:
        PATH = "drivers/chromedriver"
        df = pd.read_csv('credentials.csv')
        IMPORTED_USERNAME =  df.iloc[1,1]
        IMPORTED_PASSWORD = df.iloc[1,2]

        #to enable automation in the background
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(PATH,options=chrome_options)

        driver.get("https://discord.com/channels/@me")
        username = driver.find_element_by_name("email")
        time.sleep(1)
        username.send_keys(IMPORTED_USERNAME)
        time.sleep(0.5)

        password = driver.find_element_by_name("password")
        password.send_keys(IMPORTED_PASSWORD)
        time.sleep(0.5)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        
        reciever = driver.find_element_by_class_name("searchBarComponent-3N7dCG")
        #.click() clicks on the button selected 
        time.sleep(0.5)
        reciever.click()
        time.sleep(0.5)
        reciever = driver.find_element_by_class_name("input-3r5zZY")
        time.sleep(0.5)
        reciever.send_keys(recepient)
        time.sleep(0.2)
        reciever.send_keys(Keys.RETURN)
        time.sleep(0.2)
        sender = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]")
        sender.send_keys(msg)
        sender.send_keys(Keys.RETURN)
        print("discord: success")
        return True
    except:
        print("discord: fail")
        return False

def send_email(msg: str, reciever: str) -> bool:
    if reciever == None or msg == "":
        return
    try:
        df = pd.read_csv('credentials.csv')
        IMPORTED_USERNAME =  df.iloc[0,1]
        print(IMPORTED_USERNAME)
        IMPORTED_PASSWORD= df.iloc[0,2]
        print(IMPORTED_PASSWORD)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(IMPORTED_USERNAME, IMPORTED_PASSWORD)

        server.sendmail(IMPORTED_USERNAME, reciever, msg)
        print('email: success')
        return True
    except:
        print("email: fail")
        return False
if __name__ == '__main__':
    send_to_discord("ahamed", "lol, ball drooler")