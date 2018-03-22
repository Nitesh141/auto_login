from selenium import webdriver
import urllib
import time
import os


def close_psiphon():
    try:
        os.system('TASKKILL /IM psiphon3.exe')
    except Exception, e:
        print str(e)


def is_connected():
    try :
        stri = "http://www.google.co.in"
        data = urllib.urlopen(stri)
        return True
    except :
        return False


def is_connected_psiphon():
    try :
        stri = "http://192.168.1.5:8090/httpclient.html"
        data = urllib.urlopen(stri)
        return True
    except :
        return False



def func():
    usr = ["pp19@iitbbs.ac.in","ss55@iitbbs.ac.in","gs15@iitbbs.ac.in","jm11@iitbbs.ac.in","mm11@iitbbs.ac.in","rs15@iitbbs.ac.in","sr16@iitbbs.ac.in","ss29@iitbbs.ac.in","nk14@iitbbs.ac.in","sv14@iitbbs.ac.in"]
    pwd = ["pp19.pp19.pp19","ss55.ss55.ss55","gs15.gs15.gs15","260799","260799","260799","260799","260799","ss55pp19gs15","xiaomi98"]

    count = 0;

    while 1==1:
        time.sleep(5)
        a = is_connected()
        b = is_connected_psiphon()
        print a," ",b
        if a and b:
            print "Net is working :)  on   ",
            print time.ctime()
            

        elif a == True and b == False:
            print "Net is working and psiphon is connected"
            
        

        elif a==False and b == False:
            close_psiphon()
            if a==False and b == False:
                print "Looks like ethernet cable is not pluggrd in!"
                
            else:
                print("Net not working :(")
                print("Attempting to login...!!!")
                driver = webdriver.Chrome('C:\Users\mibaa\Downloads\chromedriver.exe')
                driver.get('http://192.168.1.5:8090/httpclient.html')

                username_box = driver.find_element_by_id('username')
                username_box.send_keys(usr[count])

                password_box = driver.find_element_by_id('password')
                password_box.send_keys(pwd[count])

                login_btn = driver.find_element_by_id('loginbutton').click()

                print("logged in at     "),
                print time.ctime(),
                print ("     using "),
                print usr[count]
                print("\n\n")
                count = count + 1
                driver.close()
                driver.quit()

        elif a==False and b == True:
            print("Net not working :(")
            print("Attempting to login...!!!")
            driver = webdriver.Chrome('C:\Users\mibaa\Downloads\chromedriver.exe')
            driver.get('http://192.168.1.5:8090/httpclient.html')

            username_box = driver.find_element_by_id('username')
            username_box.send_keys(usr[count])

            password_box = driver.find_element_by_id('password')
            password_box.send_keys(pwd[count])

            login_btn = driver.find_element_by_id('loginbutton').click()

            print("logged in at     "),
            print time.ctime(),
            print ("     using "),
            print usr[count]
            print("\n\n")
            count = count + 1
            driver.close()
            driver.quit()
        

func()

