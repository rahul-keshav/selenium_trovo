from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from basic import random_string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_path = which('chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("start-maximized")
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
driver.execute_script("window.open('about:blank', 'tab2');")
# switching to tab 2/temp mail
driver.switch_to.window("tab2")
driver.get("https://emailfake.com/")

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
user_name = random_string(7)
inputs[1].send_keys(user_name)
# sending random password
password = random_string(8)
inputs[2].send_keys(password)
# entering date of birth
month = driver.find_element_by_xpath('//div[@class="month"]')
time.sleep(2)
month.click()
feb = driver.find_element_by_xpath('(//ul[@class="dropdown-list"])[1]/li[2]')
time.sleep(2)
feb.click()

day = driver.find_element_by_xpath('//div[@class="day"]')
day.click()
two = driver.find_element_by_xpath('(//ul[@class="dropdown-list"])[2]/li[3]')
two.click()

time.sleep(5)
year = driver.find_element_by_xpath('//div[@class="year"]')
year.click()

time.sleep(5)
twoKone = driver.find_element_by_xpath('(//ul[@class="dropdown-list"])[3]/li[20]')
twoKone.click()

# final sign up button clicked
time.sleep(5)
signup_btn_big = driver.find_element_by_xpath('//button[@class="button-sign-up primary-btn"]')
signup_btn_big.click()

# wait for captcha....
k = True
while k:
    try:
        captcha_frame = driver.find_element(By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")        
        driver.switch_to.frame(captcha_frame)  
        driver.implicitly_wait(2)
        print('Frame changed')
        print('finding element')
        print('pray')        
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-anchor-container"]')))
        btn.click()
        print('button clicked')
        k= False
    except:
        k=True
        print('i am stll in')

# verification....
print('No i am out')



driver.implicitly_wait(60)
