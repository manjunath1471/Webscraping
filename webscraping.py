#                                             *** WEB SCRAPING ***
#  web scraping is a software technique of extracting informaton from websites. This technique mostly focuses on the transformation of unstructred data (html format) on the web into structured data ( database or spreadsheet)
# webpage website (HTML format) ---> web scraping --->  data 

# Libraraies used for web scraping :
# BeautifulSoup : it is a tool for pulling out information from a webpage. You can use to extract tables,files,paragraph and you can also put filters to extract information from web pages

# PIP :
# PIP is a package manager for python packages
# For installation : 
# pip install package/library/framework
# for uninstallation :
# pip uninstall package/library/framework

# Installed libraries :
# 1. BeautifulSoup
# 2. requests
# 3. pandas
'''
# Import section : import required libraries for scraping
import requests
import pandas as p
from bs4 import BeautifulSoup

# requesting and confirming scraping
response=requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_f02ba52f-267c-4d9b-9b7b-6af35258beb5_5.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=odk4g28ekg0000001681046442724')
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
                         # *** flipkart web scraping - done *** #
                           
                           
                            # *** structure the data ***
                           


# names of phones (realme)

names=soup.find_all('div',class_='_4rR01T')
#print(names)
name=[]
for a in names:
    b=a.get_text()
    name.append(b)
print(name)


# prices of phones

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
#print(prices)
price=[]
for c in prices:
    d=c.get_text()
    price.append(d)
print(price)


# ratings of phones

ratings=soup.find_all('div',class_='_3LWZlK')
#print(ratings)
rate=[]
for e in ratings:
    f=e.get_text()
    rate.append(float(f))
print(rate)


# images of phones

images=soup.find_all('img',class_='_396cs4')
#print(ratings)
image=[]
for g in images:
    h=g['src']
    image.append(h)
print(image)

# links

links=soup.find_all('a',class_='_1fQZEK')
#print(links)
link=[]
for i in links:
    j="https://www.flipkart.com" + i['href']
    link.append(j)
print(link)


                           
                             # *** storing the structered data in a file ***




# storing the structered data   ---->   data frame (excel form)
df=p.DataFrame()
#print(df)
df['Names']=name
df['Prices']=price
df['Rates']=rate
df['Images']=image
df['Links']=link
#print(df)
df.to_csv('realme.csv')
'''