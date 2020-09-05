#!/usr/bin/env python

import schedule  # module used to schedule jobs or tasks
import time # module used to handle time related tasks, it is 100 times better then APPScheduler because we do not need to match zone time which could results in infinite bugs!
import psutil  # module used to output system, memory, network and many other useful statistics
import win32api # module used to pop-up a window in Windows
import subprocess # module used to run system PowerShell, Shell or bash command from Python script

def automated():

  cpu_usage = psutil.cpu_percent()  # percentage of cpu used
  mem_used = psutil.virtual_memory().percent # percentage of memory used
  
  available_mem = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total # calculate the memory not in use
  av_mem = "{0:.2f}".format(available_mem) # format the float of the memory not in use to 2 decimals only after the comma

  if cpu_usage >= 80:
    win32api.MessageBox(0, 'CPU Usage is greater than 80%!!', 'Warning!') # alert if cpu usage percentage is 80% or more
  
  if mem_used >= 80: # alert if memory used is 80% or more and excecute the explained PowerShell command below 
    win32api.MessageBox(0, 'Memory usage is greater than 80%!!', 'Warning!')
    action = subprocess.run("C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe 'ipconfig/ flushdns' ", shell=True, capture_output=True) # This powershell command will discard negative cache entries from the cache, as well as any other entries that have been added dynamically, which results in decreasing the current memory use.
    print(f"The system exit code is {action.returncode} and the Powershell command executed is {action.stdout}.")
    
    # returncode == system.exit() code
    # stdout output the excecution of the powerhsell command


  

  print(f"The percentage of CPU used is {cpu_usage}%, the percentage of the current used memory is {mem_used}% and the percentage of the available memory is {av_mem}%.")
  


schedule.every(1).minutes.do(automated) # job will run every 1 minute



# Other schedule to choose from:(you can modify it to match your need such as 2 hours instead of 1 or 2 days instead of 1 ect..)

  #schedule.every(1).hour.do(automated)
  #schedule.every(1).day.at("10:30").do(automated)
  #schedule.every(5).to(10).minutes.do(automated)
  #schedule.every().monday.do(automated)
  #schedule.every().wednesday.at("13:15").do(automated)
  #schedule.every(1).minute.at(":17").do(automated)

while True:
    schedule.run_pending()
    time.sleep(1)  # time sleeping interval of one second between each time code excecution






    
  

