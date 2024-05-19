import csv
import requests
import json

def scrape_market_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = json.loads(response.content)  # Parse JSON response

        return data.get("marketPrice")  # Return marketPrice value or None if not found
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}\n{e}")
        return None

def main():
    def process_csv_files(csv_filenames):
        for filename in csv_filenames:
        # Construct the output filename
            out_filename = f"{filename}_out.csv"

            # Open input and output files with newline handling
            with open(filename, "r", newline="") as infile, open(out_filename, "w", newline="") as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)

            # Skip header and potentially row 1
                next(reader, None)
                next(reader, None)

                for row in reader:
                    print(row[0])
                    price_url = row[4]  # Assuming URL is in column E at index 4
                    price = scrape_market_price(price_url)
                    print(price)
                    if price is not None:
                        row[2] = price  # Update price in column C (index 2)

                    writer.writerow(row)
                    
    csv_files = ["bbs.csv", "bbundles.csv", "bpacks.csv", "etbs.csv"]
    process_csv_files(csv_files)

if __name__ == "__main__":
    main()