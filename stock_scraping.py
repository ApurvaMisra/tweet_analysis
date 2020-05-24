import numpy as np 
import pandas as pd 
import seaborn as sns 
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
#url from which the data has to be scrapped
link="https://ca.finance.yahoo.com/quote/TSLA/history?period1=1274486400&period2=1590105600&interval=1d&filter=history&frequency=1d"
#Using selenium to launch automated instance of chrome
driver=webdriver.Chrome()
driver.get(link)
#Letting it sleep for 50 seconds to make sure the webpage loads completely
time.sleep(50)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')
#Finding the first "table" tag with the specified class
stock_table = soup.find("table", attrs={"class": "W(100%) M(0)"})
#Finds all "tr" tags
trs = stock_table.tbody.find_all("tr")
  #Finds all "td" tags
tds=stock_table.find_all("td")
#opening a *.csv file to write in the table data
f = csv.writer(open("tesla_price.csv", "w"))
#header for the *.csv file 
f.writerow(["date", "open", "high", "low", "close", "adj_close","volume"])    
for tr in trs:
    header=[]
    for td in tr.find_all("td"):
        s=td.span.contents #getting the content 
        header.append(s[0])
    f.writerow(header)

        
