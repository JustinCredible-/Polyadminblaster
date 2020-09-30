import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=options)

IPlist = open('list.txt','r').read().split()

password = "456"
altpassword = "CHANGEME"
newpassword = "NEWPASSWORD"
def findpasswordfield():
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys(altpassword)
        driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .button").click()
        
for ip in IPlist:
    print("Checking IP: "+ip)
    url = "https://" + ip + "/"
    driver.get(url)
    polycomtest = driver.find_element(By.NAME, "password")
    if polycomtest:
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .button").click()
        time.sleep(3)
        defaultfound = []
        invalidfound = []
        loggedin = []
        defaultfound = driver.find_elements_by_xpath("//*[contains(text(), 'Default password is in use. Please change!')]")
        if not defaultfound:
            invalidfound = driver.find_elements_by_xpath("//*[contains(text(), 'Invalid password. Try again.')]")
            if not invalidfound:
                loggedin = driver.find_elements_by_xpath("//*[contains(text(), 'Logged in as')]")
        
        if  invalidfound:
            print("Default password not set. Trying alternate.")
            try:
                findpasswordfield()
                time.sleep(3)
                loggedin = driver.find_elements_by_xpath("//*[contains(text(), 'Logged in as')]")
                if not loggedin:
                    print(password+" and "+altpassword+" incorrect for " + url)
            except NoSuchElementException:
                print("Could not log into " + ip + ": element not found")
                pass
        if defaultfound or loggedin:
            print("Password found. Updating.")
            driver.find_element(By.XPATH, '//li[@id="topMenuItem4"]/a/span').click()
            driver.find_element(By.CSS_SELECTOR, "#topMenuItem4 > ul > li:nth-child(14) span").click()
            time.sleep(2)
            element = driver.find_element(By.ID, "adminPwdSaveBtn")
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            driver.find_element(By.ID, "oldadminpswd").click()
            # Default/current Admin password
            if defaultfound:
                driver.find_element(By.ID, "oldadminpswd").send_keys(password)
            elif loggedin:
                driver.find_element(By.ID, "oldadminpswd").send_keys(altpassword)
            driver.find_element(By.NAME, "newadminpswd").click()
            driver.find_element(By.NAME, "newadminpswd").send_keys(newpassword)
            driver.find_element(By.NAME, "cnfmadminpswd").click()
            driver.find_element(By.NAME, "cnfmadminpswd").send_keys(newpassword)
            driver.find_element(By.ID, "adminPwdSaveBtn").click()
            time.sleep(1)
