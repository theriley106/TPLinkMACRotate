try:
    from selenium import webdriver
    
except:
    raise Exception("Download chromedriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads")
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
driver.quit()