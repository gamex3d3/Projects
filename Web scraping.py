from urllib.request import urlopen
from bs4 import BeautifulSoup

icove_url = "https://charisgeorge14.wixsite.com/icove"

page = urlopen(icove_url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())