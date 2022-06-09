# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:34:13 2020

@author: eredm
"""

# from unicodedata import name
import requests
from bs4 import BeautifulSoup
import pandas as pd
# import csv


page = requests.get("https://research4kids.ucalgary.ca/members/directory/")

# print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
# print(type(soup))

names = []
profile_pages = []
emails = []

data = soup.findAll('div',attrs={'class':'views-element-container'})
for div in data:
    links = div.findAll('a')
    for link in links:
        # print(link.get_text())
        names.append(link.get_text())
        if link.get('href') != None:
            if 'https://' in link.get('href'):
                pass
            #     print(link.get('href'))
            else:
                cur_link = 'https://research4kids.ucalgary.ca' + link.get('href') # Convert relative URL to absolute URL
                profile_pages.append(cur_link)
                # print(cur_link)

print("---------------------------------------------------------")

print(profile_pages)

for page in profile_pages:
    cur_page = requests.get(page)
    soup = BeautifulSoup(cur_page.content, 'html.parser')
    data = soup.findAll('div',attrs={'class':'col-md-6'})
    # print(user_data[0])
    for div in data:
        links = div.findAll('a')
        for link in links:
            # print(link.get_text())
            if link.get('href') != None:
                if 'mailto:' in link.get('href'):
                    emails.append(link.get_text())
                    # print(emails)

#### Need to transpose both names and emails here!!!

data = list(zip(names, emails))
df = pd.DataFrame(data, columns = ['Name', 'Email'])
df.to_csv("Research4Kids_Members",index=False)

