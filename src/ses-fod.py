import requests
import bs4
import pyfiglet
import time


print(pyfiglet.figlet_format('SES-FOD',font='epic'))
print('Search Engine Scraping For Open Directories\n')
disclaimer='''Disclaimer:
This project is purely for academic purposes.
Some results may contain pirated and/or copyrighted content.
The author of this project condemns piracy and can not be held resposible if this project is used to find/share pirated content.
Use with caution, the listed links may be malicious. The author of this project can not be held resposible for any damages incurred due to irresponsible usage.
(Not all pages listed here will be public directories)
(If you dont know where to start, try searching for movies. For instance: The martian)\n\n'''
print(disclaimer)

while True:
    # getting the query
    text= input('Enter search query:')
    url = 'https://google.com/search?q="index of" ' + text
    #print('\n {} \n'.format(url))
    print('_'*133)
    print()

    # getting results using requests.get(url) and storing it in results
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }
    result=requests.get(url,headers=headers)
    #print(type(result))
    if '<Response [429]>' == str(result):
        print('''
  |\____/|
 /        \\
|  **  **  |
|  **  **  |
|     0    | 
|   _____  |
 \________/''')
        print('\n****Sorry, You Have Exceeded The Rate Limit. The Servers Think You Are A Robot. Try Again After Few Minutes. (SES-FOD will terminate itself in 2 minutes)****\n','_'*133)
        time.sleep(120)
        break
    


    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(result.text,"html.parser")
    #print(soup)

    atags=soup.find_all('a')
    #print(atags)
    #extracting the desired url for the directory
    for link in atags:
        if 'https' in link.get('href') and 'google' not in link.get('href'):
            print(link.get('href').split('://')[1].split('&ved=')[0],end='\n________________\n')
    print('_'*133)
    choice=input('Make another search?(y/n) ')
    if choice=='n':
        print('Thanks for using! This window will close automatically in 60 seconds.')
        time.sleep(60)
        break
    print('\n')
