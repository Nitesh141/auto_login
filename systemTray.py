
import wx
from wx import adv
from selenium import webdriver
import urllib
import time

class CustomTaskBarIcon(wx.adv.TaskBarIcon):

    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, frame):
        """Constructor"""
        wx.adv.TaskBarIcon.__init__(self)


        self.frame = frame
 
        img = wx.Image("images.png", wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(img)
        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(bmp)
 
        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
 
    #----------------------------------------------------------------------
    def OnTaskBarActivate(self, evt):
        print "OnTaskBarActivate"
        """"""
        pass
 
    #----------------------------------------------------------------------
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        print "OnTaskBarClose"
        self.frame.Close()
 
    #----------------------------------------------------------------------
    def OnTaskBarLeftClick(self, evt):
        """
        Create the right-click menu
        """
        print "OnTaskBarLeftClick"
        self.frame.Show()
        self.frame.Restore()




 
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Minimize to Tray")
        panel = wx.Panel(self)
        self.tbIcon = CustomTaskBarIcon(self)
 
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)
 
        self.Show()
 
    #----------------------------------------------------------------------
    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()
 
    #----------------------------------------------------------------------
    def onMinimize(self, event):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        if self.IsIconized():
            self.Hide()


    

def is_connected():
    try :
        stri = "https://www.google.co.in"
        data = urllib.urlopen(stri)
        return True
    except :
        return False


def func():


    usr = ["pp19@iitbbs.ac.in","ss55@iitbbs.ac.in","gs15@iitbbs.ac.in","jm11@iitbbs.ac.in","mm11@iitbbs.ac.in","rs15@iitbbs.ac.in","sr16@iitbbs.ac.in","ss29@iitbbs.ac.in","nk14@iitbbs.ac.in","sv14@iitbbs.ac.in"]
    pwd = ["pp19.pp19.pp19","ss55.ss55.ss55","gs15.gs15.gs15","260799","260799","260799","260799","260799","ss55pp19gs15","xiaomi98"]

    count = 0;

    while 1==1:
        if is_connected():
            print "Net is working :)  on   ",
            print time.ctime()
            time.sleep(10)
        

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
        






 
#----------------------------------------------------------------------
def main():
    """"""
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
    func()

    
    
 
if __name__ == "__main__":
    main()
