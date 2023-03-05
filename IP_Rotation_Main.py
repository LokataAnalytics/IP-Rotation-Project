import time
import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def load_browser(link):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    # replace with the CAPTCHA HTML text that loads in your case
    if "captcha-error-message" in browser.page_source:
        print("assigning a new IP address")
        return True
    else:
        # replace with your own browser navigation code
        print("accepting all cookies")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "accept-handler"))).click()
        # click on the cart page using cart HTML ID
        browser.find_element(By.ID, 'add-to-cart').click()
    print("success")
    
def rotate_ip_address():
    print("rotating IP")
    command = 'sudo protonvpn c -r'
    process = subprocess.Popen(command, shell=True)
    time.sleep(5)
    print("new IP assigned")
  
while True:
    if not load_browser(url):
        print("Loading url")
    else:
        print("CAPTCHA detected")
        rotate_ip_address()
