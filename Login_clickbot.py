from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentias import email,pw

# path= r'C:\Users\16075\Documents\chromedriver.exe'
# path1= r'C:\Users\16075\Documents\work\Data_harvesting\automationScrap\chromedriver.exe'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def openTinder():
        driver.get('https://tinder.com/')
        
        sleep(2)
        
        
        login = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login.click()
        sleep(2)
        print('GOING TO FACEBOOK')
        faceBook_login()
        
        sleep(4)
        driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
        print('ALLOW LOCATION')
        
        try:
            accept_cookie =driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
            accept_cookie.click()
        except:
            print('no cookies')
 
        try:
            notifcation_button= driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
            notifcation_button.click()
        except:
            print('no nofication')
        
        print('BEGIN SWIPING BRO')
        auto_swipe()
    
def faceBook_login():
        print('FACEBOOK FUNCTION BING RUN')
        login_facebook = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]")
        login_facebook.click()
        
        original_window= driver.window_handles[0]
        popUp_window= driver.window_handles[1]
        #select the popUp_window
        driver.switch_to.window(popUp_window)
        
        print('PUTING INFO INFO IN')
        email_field = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        pw_feild = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login= driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
        
        email_field.send_keys(email)
        sleep(1)
        pw_feild.send_keys(pw)
        sleep(2)
        print('---------LOGIN--------------------')
        login.click()
        
        
        print('SWITCHING BACK TO MAIN WINDOW')
        driver.switch_to.window(original_window)

def right_swipe():
    doc = driver.find_element(By.XPATH,'/html/body')
    doc.send_keys(Keys.ARROW_RIGHT)

def auto_swipe():
    while True:
        sleep(2)
        right_swipe()
      
openTinder()



