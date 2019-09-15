import requests
from bs4 import BeautifulSoup
import csv
from random import choice
import re
from csv import DictReader

base_url="http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename,"r", encoding='UTF8') as file:
        csv_reader=DictReader(file)
        return list(csv_reader)
            

def start_game(quotes1):
    quote=choice(quotes1)
    remaining_guesses=4
    print(quote["text"])
    print(quote["author"])
    guess=''
    while guess.lower() != quote["author"].lower() and remaining_guesses>0:
        guess=input(f"Who said this quote? Guesses remaining: {remaining_guesses} ")
        if guess.lower()==quote["author"].lower():
            break
        remaining_guesses-=1
        if remaining_guesses==3:
            res=requests.get(f"{base_url}{quote['bio-link']}")
            soup=BeautifulSoup(res.text, "html.parser")
            birth_date=soup.find(class_="author-born-date").get_text()
            birth_place=soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place} ")
        elif remaining_guesses==2:
            print(f"Here's a hint: The author's first name starts with {quote['author'][0]} ")

        elif remaining_guesses==1:
            last_initial=quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with {last_initial} ")
        
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']} ")

    again=''
#After 1 game.
    while again not in ('y','yes','n','no'):
        again=input("Would you like to play again (y/n)? ")
    if again.lower() in ('yes','y'):
        print("OK YOU PLAY AGAIN!")
        return start_game(quotes1)
        
    else:
        print("OK, GOODBYE!")


    
quotes1= read_quotes("quotes.csv")
start_game(quotes1)
