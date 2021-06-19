from pynytimes import NYTAPI
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
from datetime import date

today = date.today()
filename = "NYT-Reviews-" + str(today) + ".txt"
f = open(filename, "a")

def getBooksRank(book, genre):
    print("\n~~~NYT ",genre," Best sellers list~~~",file=f)
    print("---------------------------------------",file=f)
    print("Rank - Title - Description",file=f)
    print("---------------------------------------",file=f)
    print("")
    for i in range(len(books)):
        print(books[i]['rank'], end=" ",file=f)
        print(books[i]['title'],file=f)
        print(books[i]['description'],file=f)
        if(books[i]['book_review_link'] != ''):
            print("NYT Rewiew Available!",file=f)
        else:
            print("NYT Review Unavailable",file=f)
        print("Goodreads rating: ",getGoodreadsRating(books[i]['title']),file=f)
        print("",file=f)

def getGoodreadsRating(book):
    url= "https://www.goodreads.com/search?q="+book 
    page = requests.get(url) 
    soup = bs(page.content, 'html.parser') 

    # find a list of all span elements
    spans = soup.find_all('span', {'class' : 'minirating'})

    # create a list of lines corresponding to element texts
    lines = [span.get_text() for span in spans]
    if (len(lines) != 0):
        return lines[0]
    else:
        return "Not Found"

API_Key = input("Enter NYT API Key : ")

try:
    nyt = NYTAPI(API_Key, parse_dates=True)
except ValueError as e:
    print("Cannot connect to NYT ")

books = nyt.best_sellers_list(
    name="combined-print-and-e-book-nonfiction"
)

print("Fetching NYT Non-Fiction Bestsellers List...")
getBooksRank(books,"Non-Fiction")

books = nyt.best_sellers_list()
print("Fetching NYT Fiction Bestsellers List...")
getBooksRank(books,"Fiction")
f.close()

while(1):
    print("~~~Get Book Review~~~~")
    booktitle = input("Enter book title: ")
    reviews = nyt.book_reviews(title=booktitle)
    if(len(reviews) != 0):
        webbrowser.open(reviews[0]['url'], new=2)
    else:
        print("No review found for book title - ", booktitle)
