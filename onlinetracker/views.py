from django.shortcuts import render
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import threading
import os
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
# chromedriver_binary
from django.http import HttpResponse

# def notifi(request):
    
#     while True:
#         current_time= time.strftime("%H:%M:%S")
#         if 7==7:
#             break
#         else:
#             pass
#     hr=ToastNotifier()
#     hr.show_toast('online','he is online')
    

def tracker(request):
    if request.method=='POST':
            TARGET=request.POST['name']


            # browser = webdriver.Chrome('C:/Users/HOME/Desktop/Chromedriver')
            # browser.get('https://web.whatsapp.com/')


            from selenium import webdriver
            from webdriver_manager.chrome import ChromeDriverManager

            gChromeOptions = webdriver.ChromeOptions()
            gChromeOptions.add_argument("window-size=1920x1480")
            gChromeOptions.add_argument("disable-dev-shm-usage")
            browser = webdriver.Chrome(
                chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
            )
            browser.get("https://web.whatsapp.com/")
            
            

            def bb():
                    time.sleep(30)
                    search = browser.find_element_by_class_name('_2_1wd')
               
                    
                    search.send_keys(TARGET)
                    time.sleep(5)
                    user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(TARGET))
                    user.click()


                    def printit():
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        current_time2 = time.strftime("%H-%M-%S", t)

                        threading.Timer(30.0, printit).start()


                        try :
                            online = browser.find_element_by_class_name('_7yrSq')            
                            #time.sleep(30)
                            if online == 'online':
                                print(TARGET + " is online")
                            else:
                                print(TARGET + " is online")
                                print(current_time)
                            
                                f = open("time.txt", "a+")
                                f = open("time.txt", "a+")
                                f.write(str(current_time2))
                                f.write("  ,  online\n")
                                f.close()
                            
                            # hr=ToastNotifier()
                            # hr.show_toast('online',TARGET + 'is online')
                            
                        except NoSuchElementException:
                                print(TARGET + " is offline")
                                print(current_time)

                                f = open("time.txt", "a+")
                                f.write(str(current_time2))
                                f.write("  ,  offline\n")
                                f.close()
                    printit()
            bb()
            
            

    return render(request,'onlinetracker/onlinetracker.html')