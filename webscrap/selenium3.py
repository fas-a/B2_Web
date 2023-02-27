import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

#import driver browser, sesuaikan lokasi driver browsernya
driver = webdriver.Chrome('D:\App\chromedriver_win32\chromedriver.exe')

#import link website
driver.get('https://www.metacritic.com/browse/games/score/metascore/all/all/filtered')
#dictionari tempat menyimpan data
result = []
i = 1;
while i < 201:
    for list in driver.find_elements(By.CSS_SELECTOR, "tr:not(.spacer)"):
        id = i
        #mengambil waktu system
        current_time = time.ctime()
        #mengambil score game
        rating = list.find_element(By.CLASS_NAME,"clamp-score-wrap").text
        #mengambil judul game
        name = list.find_element(By.TAG_NAME,"h3").text
        #mengambil jenis plathfrom game
        plathfrom = list.find_element(By.CSS_SELECTOR,"span.data").text
        #mengambil tanggal release game
        release = list.find_element(By.XPATH, "//div[@class='clamp-details']/span[not(@class)]").text
        #mengambil tag img game
        img = list.find_element(By.CSS_SELECTOR, "td.clamp-image-wrap a").find_element(By.TAG_NAME, "img")
        #mengambil atribut src dari img
        srcimg = img.get_attribute("src")
        #menyimpan img ke penyimpanan
        urllib.request.urlretrieve(srcimg, str(i)+".png")
        #menyimpan data ke dictionary
        result.append({"id":i, "judul":name, "release":release,
                       "plathfrom":plathfrom, "rate":rating, "img":srcimg,"waktu_scraping":current_time})
        print(i)
        i = i + 1
    #pindah next page
    driver.find_element(By.PARTIAL_LINK_TEXT, "next").click()
driver.quit()
#menyimpan data ke file json
HasilJSON = json.dumps(result)
JSONFile = open("TopGames.json", "w")
JSONFile.write(HasilJSON)
JSONFile.close()
