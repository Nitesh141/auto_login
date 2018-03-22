from selenium import webdriver
import urllib
import time

def is_connected():
    try :
        stri = "https://www.google.co.in"
        data = urllib.urlopen(stri)
        return True
    except :
        return False





        

    
driver = webdriver.Chrome('C:\Users\mibaa\Downloads\chromedriver.exe')
driver.get('https://www.geeksforgeeks.org')

#username_box = driver.find_element_by_id('username')
#username_box.send_keys(usr[count])

#password_box = driver.find_element_by_id('password')
#password_box.send_keys(pwd[count])

#login_btn = driver.find_element_by_id('loginbutton').click()
#count = count + 1
#driver.close()
#####driver.quit()
        

