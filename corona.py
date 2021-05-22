import requests 
from bs4 import BeautifulSoup
from plyer import notification
import time


res = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find('div',{'class':'maincounter-number'}).get_text().strip()
#deaths = soup.find('div',{'id':'maincounter-wrap'}).get_text().strip()
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 5
            )

while True:
    notifyMe('Total Corona cases are :',cases)
    time.sleep(4)
    #notifyMe('Total casres is:',deaths)
    #time.sleep(4)
    exit()

