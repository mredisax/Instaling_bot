from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
import re
import time
#Firefox browser = webdriver.Firefox('./geckodriver')
def session(username, passwd):
    try:
        browser = webdriver.Chrome('./chromedriver')
        browser.get('https://instaling.pl/teacher.php?page=login')

        #LOGIN  
        login = browser.find_element_by_xpath('//*[@id="log_email"]')
        password = browser.find_element_by_xpath('//*[@id="log_password"]')
        login_button = browser.find_element_by_xpath('/html/body/div/div[2]/div/form/input[5]')
        login.send_keys(username)    
        password.send_keys(passwd)
        login_button.click()
        time.sleep(1)

    #ENTRY TO SESSION
        entry_to_session = browser.find_element_by_xpath('//*[@id="session_button"]').click()
        time.sleep(1)
        session_button = browser.find_element_by_xpath('//*[@id="continue_session_button"]/h4')
        if session_button.is_displayed():
            #print('continue_session')
            time.sleep(2)
            session_button.click()
        else:
            time.sleep(2)
            #print('start_session')
            session = browser.find_element_by_xpath('//*[@id="start_session_button"]/h4').click()
        input_word = browser.find_element_by_xpath('//*[@id="answer"]')
        check_word = browser.find_element_by_xpath('//*[@id="check"]/h4')
        next_word = browser.find_element_by_xpath('//*[@id="next_word"]')
        know_new = browser.find_element_by_xpath('//*[@id="dont_know_new"]/h4')
        
    #GET WORD FROM CODE WEBSITE AND INPUT
        if input_word: 
            while True:
                time.sleep(0.5)
                if know_new.is_displayed():
                    time.sleep(1)
                    know_new.click()
                    skip_word = browser.find_element_by_xpath('//*[@id="skip"]').click()
                else:
                    time.sleep(2)
                    mp3 = browser.find_element_by_xpath('//*[@id="jp_audio_0"]').get_attribute("src")
                    re_mp3 = re.compile(r'https://instaling.pl//mp3/\d/')
                    re_word = re_mp3.sub('', mp3)
                    word = re_word.replace('.mp3', '')
                    word = str(word)
                    if word.find('%20'):
                        word2 = word.replace('%20', ' ')
                        print(word2)
                        time.sleep(1.5)
                        input_word.send_keys(word2)
                    else:    
                        time.sleep(1.5)
                        input_word.send_keys(word)
                    check_word.click()
                    time.sleep(1)
                    next_word.click()
        #390108233
        #zfyop
        time.sleep(1)
        browser.quit()
    except:
        time.sleep(30)
        print('Wystąpił Błąd')
        browser.quit()

with open('config.txt') as f:
    login = f.readline().rstrip()
    password = f.readline().rstrip()
session(login, password)