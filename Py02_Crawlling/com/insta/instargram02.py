# -*- coding:utf-8 -*-

# 설치
# pip install seleninum


from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.instagram.com/explore/tags/'+input('search tag:')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

# options = 크롬안뜨게 해달라는 것 
driver = webdriver.Chrome('c:/test/chromedriver.exe',options=options)
driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')

print(soup.find('div',{'class','KL4Bh'}))