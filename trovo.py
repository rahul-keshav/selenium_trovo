from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from basic import random_string,user_name,save_cred
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import requests
from selenium.webdriver.common.action_chains import ActionChains



chrome_path = which('chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
chrome_options.add_argument("start-maximized")
chrome_options.ensure_clean_session = True
# chrome_options.add_argument("--window-size=800,600")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)




driver = webdriver.Chrome(executable_path = chrome_path,options=chrome_options)

# /* opening trovo.live*/
driver.get("https://trovo.live/",)
wait = WebDriverWait(driver,20)
log_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='cat-button normal primary']")))
time.sleep(5)
log_in_btn.click()
check = True
while check:
    try:
        signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="header-tab"]/li[2]'))) 
        time.sleep(5)
        signup_btn.click()
        check = False
    except:
        wait = WebDriverWait(driver,20)
        log_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='cat-button normal primary']")))
        signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="header-tab"]/li[2]')))
        time.sleep(5)
        signup_btn.click()


# opening temp mail
time.sleep(1)
driver.execute_script("window.open('about:blank', 'tab2');")
# switching to tab 2/temp mail
time.sleep(1)
driver.switch_to.window("tab2")
time.sleep(2)
driver.get("https://emailfake.com/")
time.sleep(3)
email = driver.find_element_by_xpath('//span[@id="email_ch_text"]')
email = email.text

# all tabs 
tabs = driver.window_handles

# switching back to tab 1
driver.switch_to.window(tabs[0])
driver.implicitly_wait(10)
inputs = driver.find_elements_by_xpath('//div[@class="input-box border-bottom"]/input')
# sending email
inputs[0].send_keys(email)
# sending random username
user_name = user_name()
inputs[1].send_keys(user_name)
print(user_name)
# sending random password
password = random_string(8)
time.sleep(1)
inputs[2].send_keys(password)
# entering date of birth
month = driver.find_element_by_xpath('//div[@class="month"]')
time.sleep(2)
month.click()
month_path = '(//ul[@class="dropdown-list"])[1]/li[' + str(random.choice(range(1,13))) + ']'
month_submit = driver.find_element_by_xpath(month_path)
time.sleep(2)
month_submit.click()

day = driver.find_element_by_xpath('//div[@class="day"]')
day.click()
day_path = '(//ul[@class="dropdown-list"])[2]/li[' + str(random.choice(range(1,20))) + ']'
day_submit = driver.find_element_by_xpath(day_path)
time.sleep(2)
day_submit.click()


year = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/div[4]/div[1]/div[3]/div[1]/input')
year.click()
year_path = '/html/body/div[3]/div[2]/div[3]/div/div[4]/div[1]/div[3]/div[2]/ul/li[' + str(random.choice(range(25,30))) + ']'
year_submit = wait.until(EC.element_to_be_clickable((By.XPATH,year_path)))
time.sleep(2)
year_submit.click()

# final sign up button clicked
time.sleep(1)
signup_btn_big = driver.find_element_by_xpath('//button[@class="button-sign-up primary-btn"]')
signup_btn_big.click()
# 
# Solving Captcha
# 
# 2captcha section
pageurl = 'https://trovo.live/'
site_key='6LfjEMoUAAAAAPv60USWs4LxOlTmoiGf7m2skV4O'
with open(r"api_key.txt", "r") as f:
  api_key = f.read()

form = {"method": "userrecaptcha",
        "googlekey": site_key,
        "key": api_key, 
        "pageurl": pageurl, 
        "json": 1}

response = requests.post('http://2captcha.com/in.php', data=form)
request_id = response.json()['request']

url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
status = 0
while not status:
    res = requests.get(url)
    if res.json()['status']==0:
        print('status=0')
        time.sleep(3)
    else:
        requ = res.json()['request']
        print('putting captcha value')
        ks = f'___grecaptcha_cfg.clients[0].V.V.callback("{requ}");'
        driver.execute_script(ks)
        status = 1
        print('successfully executed captcha')        
        
time.sleep(10)
#tab changed to get veification key 
driver.switch_to.window(tabs[1])
driver.switch_to.default_content
k=0
while k==0:
    try:
        wait = WebDriverWait(driver,30)
        verification_path='//*[@id="email-table"]/div[2]/div[4]/div[3]/table/tbody/tr/td/div/div[3]/div/div/div[3]/div/p/span/strong'
        verification_key = wait.until(EC.presence_of_element_located((By.XPATH,verification_path))).text
        print(verification_key)
        k=1
    except:
        driver.refresh()
        k=0
        print('refreshing the browser')
        print('email not recived')
# back to tab 0 to put the verification Key
verification_key_list = list(str(verification_key))
print(verification_key_list)
driver.switch_to.window(tabs[0])
time.sleep(10)
wait = WebDriverWait(driver,30)
input_feild_1 = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div[3]/div/div/div[2]/div[1]/ul/li[1]')))
time.sleep(2)
input_feild_1.click()
print('clicked')
time.sleep(10)
actions = ActionChains(driver)
actions.send_keys(verification_key)
actions.perform()
driver.quit()
save_cred(email,user_name,password)
print('text sent!!!')
print(email)
print(user_name)
print(password)
print('data saved in "username_password.csv" file')