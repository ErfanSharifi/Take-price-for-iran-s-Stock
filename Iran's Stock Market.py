#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode
import smtplib


class Stock_Send_Mail():

    w = " "
    
    def __init__(self):
        pass 

    def Check_ShareName(self, inp):


        
        global q

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=options, executable_path= r'C:\chromedriver')
        driver.get('https://rahavard365.com/asset/547/' + inp)
        soup = BeautifulSoup(driver.page_source,"lxml")
        item = soup.find('span', {'class' : 'bold-price'})
        item = item.get_text()
        q = item

        shares = input("Please Enter Your Number of share: ")


        q = unidecode(q)
        q = q.replace(",", "")
        q = (int(q))
        shares = (int(shares))
        su = (q*shares)
        
        print ("Share name is: {0:s}".format(inp))
        print ("Your share price for today is: {0:d} Rial".format(q))
        print ("Your total capital from this share for today is: {0:d} Rial".format(su))





def main():

    
    inp = input("Please enter share name: ")
    while (inp != "fin"):
        obj = Stock_Send_Mail()
        obj.Check_ShareName(inp)
        main()

main()


