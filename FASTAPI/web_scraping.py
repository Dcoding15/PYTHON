from requests import get
from bs4 import BeautifulSoup

# Fetching Data
# req = get('https://en.wikipedia.org/wiki/Wikipedia:About')
# global fileno 
# fileno = 1
# with open(f"fetch_data_{fileno}.html", "w") as f:
#     f.write(req.text)

with open("fetch_data_1.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Title of document in string
# print(soup.title.string)

# Prettify html document
# print(soup.prettify)

# Find all div tag
# print(soup.div)

# Find all links within html document
# link = []
# for i in soup.find_all('a'):
#     link.append(i.get('href'))
# print(link)

# Find using specific id or class
# s = soup.find(id='link3')