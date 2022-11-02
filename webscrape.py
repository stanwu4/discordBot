from bs4 import BeautifulSoup
import requests

html_text = requests.get(https://stockx.com/)
soup = BeautifulSoup(html_text, 'lxml')

