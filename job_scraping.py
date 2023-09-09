import re
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import selenium
from selenium.webdriver import EdgeOptions


zip_input_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/form/div[3]/div/div/div/div[2]/input"
keyword_input_xpath = '//*[@id="KeywordFacet-input"]'
search_button_xpath = '//*[@id="findjob"]/div[6]/div/button'
web_link = "https://jobs.ksl.com/search/keywords/"
proxy = 'http://24.158.29.166:80'
search_terms = ['excel', 'python', 'data entry']
class Jobs():
    def __init__(self):
        self.driver = self.web_driver(proxy)
        self.zip_codes = self.get_Zips()
        self.search_terms = search_terms

    def web_driver(self, proxy):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('headless'),
        edge_options.add_argument('disable-gpu')
        edge_options.add_argument("--proxy_server=%s" % proxy)
        driver = selenium.webdriver.Edge(options=edge_options)
        return driver

    def get_Zips(self):
        file = open("zipcodes_backup", "r").read().strip().split('\n')
        return file

    def search_ksl(self):
        wait = WebDriverWait(self.driver, 15)
        listings = []
        for term in self.search_terms:
            self.driver.get(web_link + term)
            listing = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'listing')))
            listings = [item.text for item in listing]
            listing.append(term)
        return listings


jobs_project = Jobs()
listing = jobs_project.search_ksl()
for i in listing:
    print(i)