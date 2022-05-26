# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:34:13 2020

@author: eredm
"""

from unicodedata import name
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


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

        if link.get('href') != None:
            if 'https://' in link.get('href'):
                pass
            #     print(link.get('href'))
            else:
                cur_link = 'https://research4kids.ucalgary.ca' + link.get('href') # Convert relative URL to absolute URL
                profile_pages.append(cur_link)
                # print(cur_link)

print("---------------------------------------------------------")
# print(profile_pages)

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

data = [names,emails]
df = pd.DataFrame(data, columns = ['Name', 'Email'])
df.to_csv(index=False)



        # emails.append(links.get_text())
        # print(links[0].get_text())

# links = soup.select('a')
# profile_pages = []

# for link in links:
#     # print(link.get_text())
#     if link.get('href') != None:
#         if 'https://' in link.get('href'):
#             pass
#         #     print(link.get('href'))
#         else:
#             cur_link = 'https://research4kids.ucalgary.ca' + link.get('href') # Convert relative URL to absolute URL
#             profile_pages.append(cur_link)
#             # print(dir(cur_link))

# card = soup.find("js-view-dom-id-8c61980a0291113506c9e39a1a8d33f5e9e61651f1b40c4b27189cab8bfc3d4c")
# card = []
# card = soup.find_all(class_="text-chunk")

# print(soup.find('p', class_='title').get_text())

# for word in soup.find_all('a'):
     # # print(type(word))

#     find_all_example=word.get_text()
  
    # Print the text obtained received 
    # in previous step
    # print(find_all_example)

# print(card)


# card_items = card.find_all(class_="text-chunk")

# this_person = card_items[0]

# print(this_person.prettify())

# period = this_person.find(class_="period-name").get_text()
# print(period)

# # period_tags = this_person.select(".tombstone-container .period-name")
# # periods = [pt.get_text() for pt in period_tags]
# # periods

# # short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

# # weather = pd.DataFrame({
# #     "period": periods,
# #     "short_desc": short_descs,
# #     "temp": temps,
# #     "desc":descs
# # })
# # weather

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# page = requests.get("https://www.ualberta.ca/computing-science/faculty-and-staff/faculty")

# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

# soup.select("tr")[1].get_text()

# card = soup.find("tr")

# card_tags = soup.select("td")
# # card_items.find_all("td")


# email= [email.get_text() for email in card_tags]

# def hasNumbers(inputString):
#      return any(char.isdigit() for char in inputString)

# def removeNonAlpha(inputString):
#     temp = ''
#     for char in inputString:
#         if char.isalpha():
#             temp += char
#     return temp

# real_emails = []
# for x in range(len(email)):
#     if x % 4 == 0:
#         temp = email[x-1]
#         if hasNumbers(temp) == True:
#            removeNonAlpha(temp) 
#         else:    
#             real_emails.append(temp)

# # with open("C:\Users\eredm\webscraping", "wb") as csv_file:
#         # writer = csv.writer(csv_file, delimiter=',')
#         # for line in real_emails:
#         #     writer.writerow(line)