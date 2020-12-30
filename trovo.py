from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from basic import random_string,user_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import requests


chrome_path = which('chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991")
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
# log_in_btn = driver.find_element_by_xpath("//button[@class='cat-button normal primary']")
time.sleep(5)
log_in_btn.click()
check = True
while check:
    try:
        signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="header-tab"]/li[2]'))) 
        # signup_btn = driver.find_element_by_xpath('//ul[@class="header-tab"]/li[2]')
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
inputs[2].send_keys(password)
# entering date of birth
month = driver.find_element_by_xpath('//div[@class="month"]')
time.sleep(2)
month.click()
month_path = '(//ul[@class="dropdown-list"])[1]/li[' + str(random.choice(range(1,13))) + ']'
month_ = driver.find_element_by_xpath(month_path)
time.sleep(2)
month_.click()

day = driver.find_element_by_xpath('//div[@class="day"]')
day.click()
day_path = '(//ul[@class="dropdown-list"])[2]/li[' + str(random.choice(range(1,20))) + ']'
two = driver.find_element_by_xpath(day_path)
two.click()


year = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/div[4]/div[1]/div[3]/div[1]/input')
year.click()
year_path = '/html/body/div[3]/div[2]/div[3]/div/div[4]/div[1]/div[3]/div[2]/ul/li[' + str(random.choice(range(25,30))) + ']'
twoKone = wait.until(EC.element_to_be_clickable((By.XPATH,year_path)))
twoKone.click()

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

# 2 captcha section ended  

# wait for captcha....
k = True
p=0

    
captcha_frame = driver.find_element(By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")        
driver.switch_to.frame(captcha_frame)
print('frame changed !!!')
# 
# 2captcha section
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
        wait = WebDriverWait(driver,60)
        text_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="g-recaptcha-response"]')))    
        print(text_element)  
        print(requ)
        print('element found')  
        js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
        ks = f'___grecaptcha_cfg.clients[0].V.V.callback();'
        print(js)
        driver.execute_script(js)
        driver.execute_script(ks)
        # driver.find_element_by_xpath('//*[@id="g-recaptcha-response"]').send_keys(Keys.ENTER)
        status = 1
        print('status =1')
        print('awesome')
        print('Now i am going for leave')
        print('last script')
        print('good night')
        print('captcha passed')

# verification....
# try:
#     time.sleep(3)
#     e_t_t = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/p')
#     print('captcha passed')
#     print(e_t_t.text)
#     submit_again = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/div/button')
#     submit_again.click()
# except:
#     print('still stuck in captcha')



driver.implicitly_wait(60)
# driver.quit()
