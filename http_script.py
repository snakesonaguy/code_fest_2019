
#####################################################################################
## THE BSHTG WILL ATTEMPT SIMPLE GET REQUESTS TO WEBSITES LISTED IN THE websites.txt
## FILE.  THE HTTP RETURN STATUS IS DISPLAYED.  THE SLEEP TIMER ACCOMPLISHES TWO 
## THINGS: FIRSTLY TO NORMALIZE TRAFFIC PATTERS TO A MORE RANDOM DISTRIBUTION, SECON-
## DLY TO DECREASE THE RISK OF APPEARING MALICIOUS (IPS DEVICES MAY TRIP FOR TOO MANY
## INBOUND REQUESTS WITHIN A CERTAIN WINDOW. 
#####################################################################################


import urllib3
import random
import time


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


print '############ WELCOME TO THE BLAZE SIMPLE HTTP TRAFFIC GENERATOR ############'
print '############# YOU CAN LIST WEBSITES IN THE \'websites.txt\' FILE #############'

in_file = open('websites.txt', 'r')

sites = []

http = urllib3.PoolManager()

for line in in_file:
    if (line == '') or (line == '\n'):
        break
    site = line.strip('\n')
    sites.append(site)

in_file.close()

limit = len(sites) - 1



while True:
    index = random.randint(0, limit)
    dest = sites[index]
    timer = random.randint(2, 4)
    print 'Attempting GET to: ' + dest
    try:
        req = http.request('GET', dest)
        req.close()
        status = req.status
        print 'Received Status: ' + str(status)

    except:
        print 'Error reaching: ' + dest

    print 'Waiting ' + str(timer) + ' Seconds.'
    time.sleep(timer)







