import requests
import json
import time
from bs4 import BeautifulSoup
URL = "https://bola.kompas.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser") 
latest = soup.find_all(class_="latest latest--news mt2 clearfix")
title1 = latest[0].find_all("a", class_="article__link")
title2 = latest[1].find_all("a", class_="article__link")
date1 = latest[0].find_all(class_="article__date")
date2 = latest[1].find_all(class_="article__date")
kategori1 = latest[0].find_all("h2", class_="article__subtitle")
kategori2 = latest[1].find_all("h2", class_="article__subtitle")
result = []
for i in range(len(title1) + len(title2)):
    current_time = time.ctime()
    if i < len(title1) :
        result.append({"id":i+1,"judul":title1[i].text.strip(),
                   "waktu":date1[i].text.strip()
                       , "kategori":kategori1[i].text.strip(),
                       "waktu_scraping":current_time})
    else :
        result.append({"id":i+1,"judul":title2[i- len(title1)].text.strip(),
                   "waktu":date2[i- len(title1)].text.strip()
                       , "kategori":kategori1[i - len(title1)].text.strip(),
                       "waktu_scraping":current_time})
HasilJSON = json.dumps(result)
JSONFile = open("BeritaTerkini.json","w")
JSONFile.write(HasilJSON)
JSONFile.close()
