# This script performs web scraping tasks on a given URL.
# It provides options to scrape data, links, and save data as CSV or text files.

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

print("Enter The url -- ex: https://facebook.com")
url = input("Enter the url : ")
get_req = requests.get(url)
webpage = bs(get_req.content, "html.parser")

prompt = "for Scrap all data into Text format : Type 1.\n"
prompt += "for Scrap all data into HTML format : Type 2.\n"
prompt += "for Scrap all link into text format : Type 3.\n"
prompt += "find all HTML tag and scrap data using tag : Type 4\n"
prompt += "for save table data into CSV file: Type 5.\n"
prompt += "for save table data into TEXT file: Type 6.\n"
print(prompt)

user = int(input("Please choose any option given below -: "))
if user < 1 or user > 6:
    print("Invalid option. Please choose a valid option.\n")
    exit()

ls_data = []
modify_data = []


while True:
    try:
        if user == 1:
            # Print scraped data as plain text
            print(webpage.text)
        elif user == 2:
            # Print scraped data as HTML
            print(webpage.prettify())
        elif user == 3:
            # Print scraped Anchor as Link
            links = webpage.find_all('a')
            for link in links:
                if link.get('href') != '#':
                    print(link.get('href'))
        elif user == 4:
            # Print scraped unique data as HTML Tag
            print(sorted(set([tag.name for tag in webpage.find_all(True)])))
            tag = input('\nWrite a tag name that you want to scrap -: ')
            for tag in webpage.find_all(tag):
                print(tag.text.strip())
            break
        elif user == 5:
            # save CSV File of table content
            for table in webpage.find_all('table'):
                for rows in table.find_all('tr'):
                    # ls_data.append(rows.text)
                    modify_data.append(filter(bool, rows.text.splitlines()))
            df = pd.DataFrame(data=modify_data)
            df.to_csv('web_scarping.csv', index=False)
            print('Your CSV file is saved successfully!')
            break
        elif user == 6:
            # save Text File of table content
            for table in webpage.find_all('table'):
                for rows in table.find_all('tr'):
                    ls_data.append(rows.text)
            for ls in ls_data:
                modify_data.append(filter(bool, ls.splitlines()))
            filename = 'scrapping.txt'
            tb = webpage.table
            with open(filename, 'w') as f:
                f.write(str(tb.get_text()))
                print('Your TEXT file is saved successfully!')
            break
    except Exception as e:
        print("An error occurred:", str(e))
