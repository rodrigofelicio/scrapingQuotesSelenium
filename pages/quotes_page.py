#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    #def __init__(self, page):
        #self.soup = BeautifulSoup(page, 'html.parser')
    def __init__(self, browser):
        self.browser = browser
    
    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        #quote_tags = self.soup.select(locator)
        #return [QuoteParser(e) for e in quote_tags]
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(e)for e in quote_tags]