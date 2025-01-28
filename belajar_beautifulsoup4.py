from urllib.request import urlopen
from bs4 import BeautifulSoup

# Pengambilan konten
url = "http://preline.co/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)
print(soup.title.string)
print(soup.get(key="Preline"))