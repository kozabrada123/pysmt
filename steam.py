import cfg
#import output can't circular import lmao

def print_out(out, color):


    print("")
    print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" + color, out, colorama.Style.RESET_ALL)


logged_in = False


import colorama

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

import time
import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




woptions = webdriver.ChromeOptions()
woptions.add_argument('--disable-blink-features=AutomationControlled')
woptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/87.0.4280.88 Safari/537.36")

#Might work better with / without??? Idk
#woptions.add_experimental_option("excludeSwitches", ["enable-automation"])
#woptions.add_experimental_option('useAutomationExtension', False)

#For headless
woptions.add_argument('--headless')
woptions.add_argument('--disable-gpu')  # Last I checked this was necessary.


w2options = webdriver.ChromeOptions()
w2options.add_argument('--disable-blink-features=AutomationControlled')
w2options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/87.0.4280.88 Safari/537.36")

#Might work better with / without??? Idk
w2options.add_experimental_option("excludeSwitches", ["enable-automation"])
w2options.add_experimental_option('useAutomationExtension', False)

#For headless
#w2options.add_argument('--headless')
#w2options.add_argument('--disable-gpu')  # Last I checked this was necessary.



#def start_driver():
#    #On my linux
#    driver = webdriver.Chrome(options=woptions, executable_path="/home/koza1brada/ChromeDriver/chromedriver")#

    #Normally can just be
    #driver = webdriver.Chrome(options=woptions)
    #return driver


#On my linux
driver = webdriver.Chrome(options=woptions, executable_path="/home/koza1brada/ChromeDriver/chromedriver")#

#Normally can just be
#driver = webdriver.Chrome(options=woptions)

#Login until it works..



#Main login to steam code, calls getProtonCode
def login():
    global logged_in

    username, password, email, emailpassword, mailprovider, emailmode = cfg.loadEncryptedCFG()

    print_out("Logging into steam..." , colorama.Fore.CYAN)


    driver.get("https://store.steampowered.com/login/")

    #Write username
    element = driver.find_element(By.ID, "input_username")
    element.click()
    element.send_keys(username)

    #Write password
    element = driver.find_element(By.ID, "input_password")
    element.click()
    element.send_keys(password)

    #Check remember me
    #element = driver.find_element(By.ID, "remember_login")
    #element.click()

    #Click sign in
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//Button[@class='btn_blue_steamui btn_medium login_btn']"))).click()


    #Wait a second
    #driver.implicitly_wait(5) bad function that I hate
    time.sleep(5)






    try:
        element = driver.find_element(By.XPATH, '//*[@id="authcode"]')

    


    except:
        #Couldnt find element, logged in
        print_out("Logged in..", colorama.Fore.CYAN)
        logged_in = True
        return 100


    else:
        if not emailmode:
            print_out("Please enter email code:", colorama.Fore.CYAN)
            code = input()

            #Enter code
            element = driver.find_element(By.XPATH, '//*[@id="authcode"]')
            element.click()
            element.clear()
            element.send_keys(code)

            #Click submit
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]"))).click()
            

            time.sleep(2)


            if driver.find_element(By.XPATH, '//*[@id="authcode"]').is_displayed():


                #while I want to try again button
                while driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div/form/div[4]/div[4]/div[1]').is_displayed():
                    print_out("Ooops, that wasnt right. Try again?:", colorama.Fore.CYAN)
                    code = input()

                    #Enter code
                    driver.find_element(By.XPATH, '//*[@id="authcode"]')
            
                    element.click()
                    element.clear()
                    element.send_keys(code)

                    #Click submit
                    wait = WebDriverWait(driver, 20)
                    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]"))).click()
                    time.sleep(2)
            

            wait = WebDriverWait(driver, 20)
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[text()='Proceed to Steam!'])"))).click()

            print_out("Logged in..", colorama.Fore.CYAN)
            logged_in = True
            return 100


        elif emailmode and mailprovider == "protonmail":
            code = getProtonCode()

            #Enter code
            driver.find_element(By.XPATH, '//*[@id="authcode"]')
            element.click()
            element.clear()
            element.send_keys(code)

            #Click submit
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]"))).click()

            

            time.sleep(2)
            


            try:
                wait = WebDriverWait(driver, 20)
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[text()='Proceed to Steam!'])"))).click()
            
            except:
                while driver.find_element(By.ID, "authcode").is_displayed():


                    print_out("Couldn't log in, invalid code?", colorama.Fore.RED)
                    #return 500

                    code = getProtonCode()

                    #Enter code
                    driver.find_element(By.XPATH, '//*[@id="authcode"]')
                    element.click()
                    element.clear()
                    element.send_keys(code)

                    #Click I want to try again
                    wait = WebDriverWait(driver, 20)
                    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[4]/div[1]/div[1]"))).click()

                    #time.sleep(3)

            else:
                print_out("Logged in..", colorama.Fore.CYAN)
                logged_in = True
                return 100

        try:
            wait = WebDriverWait(driver, 3)
            error = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="error_display"]')))
            print_out("Steam Error: " + error.text + colorama.Style.RESET_ALL)
            print_out("Most likely this is a too many invalid login requests in a short time error, wait 30 minutes and try again.")
            return 403

        except:pass


#Logins to proton, doesnt get code 1/2
def loginToProton(driver):
    username, password, email, emailpassword, mailprovider, emailmode = cfg.loadEncryptedCFG()


    driver.get("https://account.protonmail.com/login")

    #email or username input
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.ID, "username"))).click()
    element = driver.find_element(By.ID, "username")
    element.clear()
    element.send_keys(email)


    #Password input
    wait.until(EC.element_to_be_clickable((By.ID, "password"))).click()
    element = driver.find_element(By.ID, "password")
    element.clear()
    element.send_keys(emailpassword)


    #Click Sign in
    element = driver.find_element(By.CSS_SELECTOR, "button[class='button button-large button-solid-norm w100 mt1-75']")
    element.click()
    time.sleep(5)

    print_out("Logged in to protonmail..", colorama.Fore.GREEN)


#Get proton code after logged in 2/2
def getSteamCodeProton(adriver):
    
    time.sleep(5)
    htmlerboi = adriver.find_element(By.CLASS_NAME, "app-root")
    htmlerboi.click()
    actions = webdriver.ActionChains(adriver)
    #wait.until(EC.element_to_be_clickable((By.XPATH, "//*[title='noreply@steampowered.com']"))).click()
    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).perform()
    actions.key_up(Keys.CONTROL)
    actions.send_keys(Keys.ENTER).perform()

    wait = WebDriverWait(adriver, 30)
    code = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='w100']")))

    time.sleep(5)    

    #needs to switch to iframe!
    adriver.switch_to.frame(adriver.find_element(By.XPATH, "//iframe[@class='w100']"))
    #/html/body/div/div[2]/div/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td
    wait = WebDriverWait(adriver, 10)
    code = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "c-blue1")))

    return code.text
                
#Main func to get proton code, makes new driver and calls both 1/2 and 2/2
def getProtonCode():
    driverProton = webdriver.Chrome(options=w2options, executable_path="/home/koza1brada/ChromeDriver/chromedriver")

    loginToProton(driverProton)

    code = getSteamCodeProton(driverProton)

    print_out("Got email code, " + code, colorama.Fore.GREEN)

    return code

#Sets steam password after logged in
def setSteamPassword(new_password):
    username, password, email, emailpassword, mailprovider, emailmode = cfg.loadEncryptedCFG()

    if not logged_in:
        print_out("Not logged in! Log in first.", colorama.Fore.RED)
        return None

    driver.get("https://store.steampowered.com/account/")

    print_out("Changing password to " + new_password, colorama.Fore.RED)

    #Click change pass link
    element = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div[6]/div[1]/div[2]/div[2]/a').click()


    #Click email code
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="wizard_contents"]/div/a[2]'))).click()


    #Enter Verif code
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'forgot_login_code')))
    element.click()
    element.clear()
    
    if emailmode:
        element.send_keys(getProtonCode())

    else:
        print_out("Please enter email code:", colorama.Fore.CYAN)
        code = input()
        element.send_keys(code)



    #Click Continue
    element = driver.find_element(By.XPATH, '//*[@id="forgot_login_code_form"]/div[3]/input')
    element.click()


    #Enter new password
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'password_reset')))
    element.click()
    element.clear()
    element.send_keys(new_password)

    #Enter retype new password
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'password_reset_confirm')))
    element.click()
    element.clear()
    element.send_keys(new_password)

    #Click Change Password
    element = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div[3]/input')
    element.click()

    print_out("Changed password to " + new_password, colorama.Fore.RED)

    cfg.saveEncryptedCFG(username, new_password, email, emailpassword, mailprovider, emailmode)

#Sets steam profile name after logged in
def setSteamProfileName(new_profile_name):
    username, password, email, emailpassword, mailprovider, emailmode = cfg.loadEncryptedCFG()

    if not logged_in:
        print_out("Not logged in! Log in first.", colorama.Fore.RED)
        return None

    driver.get("https://steamcommunity.com/profiles/76561199162339633/edit/info")

    #Change the profile name
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application_root"]/div[2]/div[2]/form/div[3]/div[2]/div[1]/label/div[2]/input')))

    print_out(f"Changing profile name from {element.get_attribute('value')} to {new_profile_name}", colorama.Fore.YELLOW)

    element.click()
    element.clear()
    element.send_keys(new_profile_name)

    #Save
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application_root"]/div[2]/div[2]/form/div[7]/button[1]')))
    element.click()

    print_out("Set profile name to " + new_profile_name, colorama.Fore.YELLOW)

    driver.get("https://steamcommunity.com/profiles/76561199162339633")
