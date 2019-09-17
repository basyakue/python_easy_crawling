import requests
from bs4 import BeautifulSoup
 
r = requests.get("https://www.goo-net.com/cgi-bin/fsearch/goo_used_search.cgi?category=USDN&phrase=s2000&query=s2000")
 
soup = BeautifulSoup(r.content, "html.parser")
 
# ニュース一覧を抽出
print(soup.find("div","base_price").text)
