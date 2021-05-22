from pynytimes import NYTAPI
import webbrowser

API_Key = input("Enter NYT API Key : ")

try:
    nyt = NYTAPI(API_Key, parse_dates=True)
except ValueError as e:
    print("Cannot connect to NYT - ")

books = nyt.best_sellers_list(
    name="combined-print-and-e-book-nonfiction"
)

print("~~~NYT Non-Fiction Best sellers list~~~")
print("---------------------------------------")
print("Rank - Title - Description - ISBN")
print("---------------------------------------")
print("")

for i in range(len(books)):
    print(books[i]['rank'], end=" ")
    print(books[i]['title'])
    print(books[i]['description'])
    if(books[i]['book_review_link'] != ''):
        print("NYT Rewiew Available!")
    else:
        print("NYT Review Unavailable")
print("")

books = nyt.best_sellers_list()

print("~~~NYT Fiction Best sellers list~~~")
print("---------------------------------------")
print("Rank - Title - Description")
print("---------------------------------------")
print("")
for i in range(len(books)):
    print(books[i]['rank'], end=" ")
    print(books[i]['title'])
    print(books[i]['description'])

while(1):
    print("~~~Get Book Review~~~~")
    booktitle = input("Enter book title: ")
    reviews = nyt.book_reviews(title=booktitle)
    if(len(reviews) != 0):
        webbrowser.open(reviews[0]['url'], new=2)
    else:
        print("No review found for book title - ", booktitle)
