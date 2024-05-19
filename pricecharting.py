import csv
import requests
from bs4 import BeautifulSoup

def scrape_market_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        soup = BeautifulSoup(response.content, "html.parser")

        price_tag = soup.find("td", id="used_price").find("span", class_="price")
        return price_tag.text.strip() if price_tag else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}\n{e}")
        return None

def main():
    with open("input.csv", "r", newline="") as infile, open("output.csv", "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Skip the first two rows (header and potentially row 1)
        next(reader, None)  # Skip header
        next(reader, None)  # Skip potential row 1

        for row in reader:
            print(row[0])
            price_url = row[4]  # Assuming URL is in column E at index 4
            price = scrape_market_price(price_url)
            print(price)
            row[2] = price or ""  # Column C in at index 2
            writer.writerow(row)

if __name__ == "__main__":
    main()
