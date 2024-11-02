import time
import requests
from bs4 import BeautifulSoup

with open('token.txt', 'r') as file:
    # Read the entire file content
    token = file.read()

api_url = f"https://johnny-cash-api-de4ecab074cf.herokuapp.com/save/{token}"

response = requests.get("https://www.johnnycash.com/releases/song-list/")


soup = BeautifulSoup(response.text,'html.parser')

target_group=soup.find('table', class_="sortable-table")

name_album=target_group.find_all('td')

nameList = []
urlList = []
albumList = []
dateList = []

index=0
for element in name_album:
    if index%3==0:
        nameList.append(element.find('a').text)
        urlList.append(element.find('a').get('href'))
        print(element.find('a').text)
        print(element.find('a').get('href'))
    if index%3==1:
        if element.find('a') != None:
            albumList.append(element.find('a').text)
            print(element.find('a').text)
        else:
            albumList.append(element.find('em').text)
            print(element.find('em').text)
    if index%3==2:
        dateList.append(element.text.strip())
        print(element.text.strip())
        print(index)
    index = index+1
recap=False
for i in range(nameList.__len__()): #should be about 2486 if im not mistaken
    if recap:
        data_post = { 
            "name": f"{nameList[i]}",
            "date": f"{dateList[i]}",
            "album": f"{albumList[i]}",
            "url": f"{urlList[i]}"
        }
        print(i)
        post_response = requests.post(api_url, json=data_post)
        time.sleep(0.5)
    else:
        recap = (nameList[i] == "Heavy Metal (Don’t Mean Rock And Roll To Me)") #my database stopped halfway through being populated. i know the last song added so the simplest way to keep entering is just to have the populator wait till the last song in the database is reached.
        

    


