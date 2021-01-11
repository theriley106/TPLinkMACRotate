try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options
except:
    raise Exception("Download chromedriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads")

import time
import random

MAC_ADDRESS = "{0}{1}-{2}{3}"
PASSWORD = "password"
URL = "http://192.168.1.1"
HEADLESS = False

options = Options()
options.headless = HEADLESS

driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

def send_key_presses(keys, delay=.1):
    for key in keys:
        ActionChains(driver).send_keys(key).perform()
        time.sleep(delay)

def login():
    ActionChains(driver).send_keys(Key.ENTER).perform()


driver.get(URL)
time.sleep(8)

send_key_presses([Keys.TAB * 2, PASSWORD, Keys.ENTER])
time.sleep(10)

driver.find_elements_by_xpath("//*[contains(text(), 'Advanced')]")[0].click()
time.sleep(5)

driver.find_elements_by_xpath("//*[contains(text(), 'Network')]")[0].click()
time.sleep(5)

driver.find_elements_by_xpath("//*[contains(text(), 'Internet')]")[0].click()
time.sleep(5)

driver.execute_script('document.getElementById("custom-mac").click()')
time.sleep(1)

driver.execute_script('document.getElementById("custom-mac-des").value = document.getElementById("custom-mac-des").value.substring(0, 12) + "{}"'.format(MAC_ADDRESS.format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))))
time.sleep(5)

driver.execute_script('document.querySelector("#internet_mac_form > div.form-submit.button-container.submit > div > div > div > div.widget-wrap.button-wrap > button > span.text.button-text").click()')
time.sleep(10)

driver.quit()