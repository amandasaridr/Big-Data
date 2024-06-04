#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

# Query to obtain links
query = 'Joko Widodo'       #term yang akan disearch

#links = [] # Initiate empty list to capture final results
#Specify number of pages on google search, each page contains 10 links
n_pages = 10                #jumlah page

for page in range(1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10) 
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #soup = BeautifulSoup (r.text, 'html.parser')

    search = soup.find_all('div', class_ = "yuRUbf")        #melihat pada 'div class' milik halaman google search
    for h in search:
        #links.append(h.a.get('href'))
        #print(h.a.text)                 #judul diberikan tanda pagar
        print(h.a.get('href'))           #url

driver.quit()


# In[ ]:




