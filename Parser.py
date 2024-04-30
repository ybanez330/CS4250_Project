from bs4 import BeautifulSoup
from pymongo import MongoClient


def parser():
    counter = 1
    # Connect to database
    client = MongoClient("localhost", 27017)
    db = client["project"]
    collection = db["webpage"]

    # Iterate through documents
    for document in collection.find():
        # Analyze html content from collected target pages
        html_content = document['html']
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract information with class "accolades", which contains "Areas of Search"
        accolades_divs = soup.find_all('div', class_='accolades')
        if accolades_divs:
            print("Document #", counter)
            for accolades_div in accolades_divs:
                print(accolades_div.get_text(separator='\n', strip=True))
            print()
        counter += 1


if __name__ == "__main__":
    parser()
