import urllib
from bs4 import BeautifulSoup
 
htmltext = urllib.urlopen("http://www.pgr21.com/pb/pb.php?id=worldcup").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

for tag in soup.select(".tdname"):
	authors.append(tag.get_text())

for author in authors:
	print author