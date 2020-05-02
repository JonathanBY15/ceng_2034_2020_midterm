# 180709014 Jonathan Barış Yaprak
# CENG 2034 Midterm Answer

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

import os
import sys
from urllib.request import urlopen
import threading

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# TASK 1 (Print PID of itself.)
pid = os.getpid()
print("PID:",pid)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# TASK 2 (If the running OS is linux; print loadavg.)
# Print loadavg ONLY if the OS is Linux
if sys.platform.startswith("linux"):
    load1, load5, load15 = os.getloadavg()
    print("Load Avg. over the last 1 minute: ", load1)
    print("Load Avg. over the last 5 minutes: ", load5)
    print("Load Avg. over the last 15 minutes: ", load15)
else:
    print("Your OS is not Linux.")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# TASK 3 (Print “5 min loadavg” value and cpu core count. If the loadavg value is near to the cpu core count; exit the script.)
cpuCount = os.cpu_count()
if sys.platform.startswith("linux"):
    load1, load5, load15 = os.getloadavg()
    print(load5)
    print(cpuCount)
    if cpuCount-load5 < 1:
        sys.exit("The loadavg value is close to the cpu core count")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# TASK 4 (Check if the urls are valid.)
urlArray = ["https://api.github.com" , "http://bilgisayar.mu.edu.tr/", "https://www.python.org/",  "http://akrepnalan.com/ceng2034", "https://github.com/caesarsalad/wow"]

def validate_url(url):
    try:
        urlopen(url) # Uses the requests library to open the url. If the url opens, that means the url is valid.
        print(url +" is a valid url.")
    except:
        print(url +" is an invalid url.") # If the url doesn't open, there will be an exception and that means the url is invalid.

threads = [] # The threads that start will be appended to this list.
for url in urlArray:
    t = threading.Thread(target=validate_url, args=[url])
    t.start()
    threads.append(t) # Append threads to the list so they aren't called more than once.

for thread in threads:
    thread.join() # Wait for threads to terminate.

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

exit = input("Press any key to exit.")
