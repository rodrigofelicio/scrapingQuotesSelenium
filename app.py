from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#import requests
from pages.quotes_page import QuotesPage


options = Options()
service = Service(ChromeDriverManager().install())

options.add_experimental_option("detach",True)

chrome = webdriver.Chrome(service=service,options=options)
chrome.get('http://quotes.toscrape.com')
#page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)
    #print(quote.content)
    
