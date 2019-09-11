'''
Web Scraping Project
Introduction
In this project you'll be building a quotes guessing game.
When run, your program will scrape a website for a collection 
of quotes. Pick one at random and display it. 
The player will have four chances to guess who said the quote. 
After every wrong guess they'll get a hint about the author's 
identity.

Requirements
1.Create a file called `scraping_project.py` which, when run,
grabs data on every quote from the website http://quotes.toscrape.com
2.You can use `bs4` and `requests` to get the data. For each quote 
you should grab the text of the quote, the name of the person 
who said the quote, and the href of the link to the person's bio.
Store all of this information in a list.
3.Next, display the quote to the user and ask who said it. 
The player will have four guesses remaining.
4.After each incorrect guess, the number of guesses remaining 
will decrement. If the player gets to zero guesses without 
identifying the author, the player loses and the game ends. 
If the player correctly identifies the author, the player wins!
5.After every incorrect guess, the player receives a hint about the author. 
  a. For the first hint, make another request to the author's bio 
  page (this is why we originally scrape this data), and tell the 
  player the author's birth date and location.
  b.The next two hints are up to you! Some ideas: the first letter 
  of the author's first name, the first letter of the author's last 
  name, the number of letters in one of the names, etc.
6. When the game is over, ask the player if they want to play 
again. If yes, restart the game with a new quote. If no, the program 
is complete.
'''


import requests
from bs4 import BeautifulSoup
import csv
from random import choice
import re
import os


tex_auth=[]

for i in range(1,11):
    response=requests.get(f"http://quotes.toscrape.com/page/{i}")
    soup=BeautifulSoup(response.text, "html.parser")
    articles=soup.find_all("div", class_='quote')
# print(articles)
    # tex2=[]
    
    for article in articles:
        tex=article.find("span",class_='text').get_text()
        auth=article.find("small", class_='author').get_text()

        tex_auth.append([tex,auth])
        
        # print(tex)
        # tex2.append(tex, auth)
        # auth2.append(auth)
# print(tex_auth)
selected=choice(tex_auth)
selected1=selected[1]
name=selected1.split()
f_name=name[0]
l_name=name[1]
# selected1='Martin Luther King Jr.'
pattern=re.compile(r'[\'\. ]')
selected2=pattern.sub("-",selected1)
pattern2=re.compile(r'[\-]{2,}')
selected3=pattern2.sub('-',selected2)
pattern3=re.compile(r'[-]$')
selected4=pattern3.sub('',selected3)
# selected2=selected1.replace(' ','-').replace('\'','-')
# if '.' in selected1:
#     selected2=selected1.replace('.','-').replace('. ','-')

response1=requests.get(f"http://quotes.toscrape.com/author/{selected4}/")
soup1=BeautifulSoup(response1.text, "html.parser")
articles_date=soup1.find("span", class_='author-born-date').get_text()
articles_location=soup1.find("span", class_='author-born-location').get_text()


count=4
answer=selected[1]
# for i in range(4):
question1=input(f"Here's a quote:  \n\n {selected[0]} \n Who said this? Guesses remaining: {count}. ")
count -=1
if question1==answer:
    print("You guessed correctly! Congratulations!")
    question2=input("Would you like to play again (y/n)? ")
    if question2=='y':
        print("Great! Here we go again...\n\n")
        os.system('scraping.py')
        
    if question2=='n':
        print("Ok! See you next time!")

    else:
        print("You should put either y or n!")
        question2
        
else:
    if count!=0:
        question3=input(f"Here's a hint: The author was born in {articles_date} {articles_location}. \n\n Who said this? Guesses remaining: {count}. ")
        if question3==answer:
            print("You guessed correctly! Congratulations!")
            question2=input("Would you like to play again (y/n)? ")
            if question2=='y':
                print("Great! Here we go again...\n\n")
                os.system('scraping.py')
                
            if question2=='n':
                print("Ok! See you next time!")
        if question3 !=answer:
            count -=1
            question4=input(f"Here's a hint: The author's first name starts with {f_name[0]} \n\n Who said this? Guesses remaining: {count}. ")
            if question4==answer:
                print("You guessed correctly! Congratulations!")
                question2=input("Would you like to play again (y/n)? ")
                if question2=='y':
                    print("Great! Here we go again...\n\n")
                    os.system('scraping.py')
                
                if question2=='n':
                    print("Ok! See you next time!")
            if question4!=answer:
                count-=1
                question5=input(f"Here's a hint: The author's last name starts with {l_name[0]} \n\n Who said this? Guesses remaining: {count}. ")
                if question5==answer:
                    print("You guessed correctly! Congratulations!")
                    question2=input("Would you like to play again (y/n)? ")
                    if question2=='y':
                        print("Great! Here we go again...\n\n")
                        os.system('scraping.py')
                    
                    if question2=='n':
                        print("Ok! See you next time!")
                if question5!=answer:
                    print(f"Sorry, you've run out of guesses. The answer was {selected1}")



    

