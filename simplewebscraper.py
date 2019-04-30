# simplewebscraper.py

# This script is only used for information purpose to demonstrate how a simple web scraper works.
# It scrapes the IMDB page of actor Morgan Freeman (a really good actor) and returns the films in which he has acted along with the name of his character and the year the film was produced.

# Import relevant libraries
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/name/nm0000151/?ref_=nv_sr_1'
response = requests.get(url)
html = response.content

# soup = BeautifulSoup(html) Not recommended for Python 3
soup = BeautifulSoup(html, 'html.parser')

# Open file to write, read the html file using regular expressions to find div classes with id as actor and then print the relevant contents to the file
with open('file.csv', 'a') as f:
	for div in soup.findAll('div', id=re.compile('^actor-')):
		f.write(str(div.contents[1].contents[0].strip()) + "," + str(div.contents[3].contents[0].contents[0].strip()) + "," + str(div.contents[6].strip()))

# Close output stream
f.close()
