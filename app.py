from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#import requests
from pages.quotes_page import QuotesPage
from pages.quotes_page import InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    selected_tag = input("Enter your tag: ")


    options = Options()
    service = Service(ChromeDriverManager().install())

    options.add_experimental_option("detach",True)

    chrome = webdriver.Chrome(service=service,options=options)
    chrome.get('http://quotes.toscrape.com/search.aspx')
    #page_content = requests.get('http://quotes.toscrape.com').content
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, selected_tag))
    
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    
    
#for quote in page.quotes:
#    print(quote)
#    #print(quote.content)
    
#author = input("Enter the author you'd like quotes from: ")
#page.select_author(author)

#tags = page.get_available_tags()
#print('Select one of these tags: [{}]'.format(" |  ".join(tags)))  # love  |  music |  anything
#selected_tag = input("Enter your tag: ")

#page.select_tag(selected_tag)
#page.search_button.click()

#print(page.quotes) 