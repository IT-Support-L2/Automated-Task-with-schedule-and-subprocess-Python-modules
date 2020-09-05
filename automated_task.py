#!/usr/bin/env python

import schedule
import time
import psutil
import win32api
import subprocess

def automated():

  cpu_usage = psutil.cpu_percent()  
  mem_used = psutil.virtual_memory().percent
  
  available_mem = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
  av_mem = "{0:.2f}".format(available_mem)

  if cpu_usage >= 40:
    win32api.MessageBox(0, 'CPU Usage is greater than 80%!!', 'Warning!')
  
  if mem_used >= 40:
    win32api.MessageBox(0, 'Memory usage is greater than 80%!!', 'Warning')
    action = subprocess.run("C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe 'ipconfig/ flushdns' ", shell=True, capture_output=True)
    print(f"The system exit code is {action.returncode} and the Powershell command executed is {action.stdout}.")


  

  print(f"The percentage of CPU used is {cpu_usage}%, the percentage of the current used memory is {mem_used}% and the percentage of the available memory is {av_mem}%.")
  


schedule.every(1).minutes.do(automated)
#schedule.every().hour.do(automated)
#schedule.every().day.at("10:30").do(automated)
#schedule.every(5).to(10).minutes.do(automated)
#schedule.every().monday.do(automated)
#schedule.every().wednesday.at("13:15").do(automated)
#schedule.every().minute.at(":17").do(automated)

while True:
    schedule.run_pending()
    time.sleep(1)






    
  

