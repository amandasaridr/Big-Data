#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import sys, getopt
sys.stdout.reconfigure(encoding='utf-8')
import argparse
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
full_text=[]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', default='', help='input filename')
    parser.add_argument('-o', '--outfile', default='', help='output filename')
    return parser.parse_args()

def main(): 
    args = parse_args()
    outfile = args.outfile
    infile = args.infile
    
    with open (infile, 'r', encoding = 'utf-8') as f:
        content = f.read().splitlines()
    f.close()
    
    filtered_text = []  #List 2D untuk menyimpan teks yang difilter
    
    f = open(outfile, 'w', encoding = 'utf-8')
    for u in content[:3]:
        driver.get(u)
        elems = driver.find_element('tag name', 'body').text.split('\n') #Membersihkan \n agar menjadi baris
        filter_elems = [line for line in elems if len(line.split()) >= 5]  #Memfilter baris yang memiliki 5 atau lebih kata
        full_text.append(filter_elems)
    print(full_text)
    
    f.write(str(full_text))
    
    #print
    driver.close()
    f.close()    
main()


# In[ ]:




