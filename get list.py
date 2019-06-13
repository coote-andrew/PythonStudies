import requests
from bs4 import BeautifulSoup
import csv

g = csv.writer(open(r'''C:\Users\coote\Desktop\list.csv''', 'w'))
g.writerow(['Name'])

f = open (r'''C:\Users\coote\Desktop\Sonia - 2019 MD Research Project 1.html''', encoding="utf8")

soup = BeautifulSoup(f.read(), 'html.parser')

table = soup.find("td", {"id" :"ctl00_MainPlaceholder_Review_0_uc_SiteReview_MiddlePane"})

research_table = table.find('table', {"class":"rgMasterTable rgClipCells"})
research_list = research_table.find_all("tr",{"class":"rgRow SiteViewMasterItem"})


contents_list = []
for item in research_list:
    listOfTable = item.find("td",{"class":"rgSorted"})
    contents = listOfTable.find("b").text
    g.writerow([contents, expanded])
