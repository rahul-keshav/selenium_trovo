from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from basic import random_string


c_p = which('chromedriver.exe')
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# options=chrome_options
driver = webdriver.Chrome(executable_path = c_p)
# opening trovo.live
driver.get("https://trovo.live/",)
driver.implicitly_wait(20)
log_in_btn = driver.find_element_by_xpath("//button[@class='cat-button normal primary']")
log_in_btn.click()
log_in_btn.click()
driver.implicitly_wait(10)
signup_btn = driver.find_element_by_xpath('//ul[@class="header-tab"]/li[2]')
signup_btn.click()

# opening temp mail
driver.execute_script("window.open('about:blank', 'tab2');")
# switching to tab 2/temp mail
driver.switch_to.window("tab2")
driver.get("https://emailfake.com/")

email = driver.find_element_by_xpath('//span[@id="email_ch_text"]')
email = email.text

tabs = driver.window_handles


# switching back to tab 1
driver.switch_to.window(tabs[0])
driver.implicitly_wait(10)
inputs = driver.find_elements_by_xpath('//div[@class="input-box border-bottom"]/input')
# sending email
inputs[0].send_keys(email)
# sending random username
user_name = random_string(7)
inputs[1].send_keys(user_name)
# sending random password
password = random_string(8)
inputs[2].send_keys(password)

driver.implicitly_wait(60)
