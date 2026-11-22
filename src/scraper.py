import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"


# Website se data lena
response = requests.get(url)

print("Status Code:", response.status_code)


# HTML ko read karna
soup = BeautifulSoup(response.text, "html.parser")


# Saari books find karna
books = soup.find_all("article", class_="product_pod")

all_books = []

# Har book ka data print karna
for book in books:

    # Book title
    title = book.find("h3").a["title"]

    # Book price
    price = book.find("p", class_="price_color").text

    # Book rating
    rating = book.find("p", class_="star-rating")["class"][1]

    # Availability
    availability = book.find("p", class_="availability").get_text(strip=True)

    category = "Not Available"

    link = book.find("h3").a["href"]

    print("Title:", title)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)
    print("Category:", category)
    print("Link:", link)
    print("-" * 40)

    all_books.append([title, price, rating, availability, link])

print("Total Books:", len(all_books))
print(all_books[0])

df = pd.DataFrame(
    all_books,
    columns=["Title", "Price", "Rating", "Availability", "Link"]
)

df.to_csv("books.csv", index=False)

print("CSV file created successfully!")