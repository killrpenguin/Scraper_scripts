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
web_link = "https://jobs.ksl.com/"
proxy = 'http://24.158.29.166:80'
link = "https://www.zipcode.com.ng/2022/12/salt-lake-county-zip-codes-ut.html"
zips_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/article/div[3]/div[2]/div/div[1]/div[2]/table/tbody'
class Jobs():
    def __init__(self):
        self.driver = self.web_driver(proxy)
        self.zip_codes = self.get_Zips()

    def web_driver(self, proxy):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('headless'),
        edge_options.add_argument('disable-gpu')
        edge_options.add_argument("--proxy_server=%s" % proxy)
        driver = selenium.webdriver.Edge(options=edge_options)
        return driver

    def get_Zips(self):
        self.driver.get(link)
        self.driver.implicitly_wait(3)
        zips = self.driver.find_element(By.XPATH, zips_xpath).text.split('\n')
        ret_zips = []
        for zip in zips:
            zip_code = re.search("(?![a-zA-Z])\d....(?![a-zA-Z])", zip).group()
            ret_zips.append(zip_code)
        return ret_zips

    def save_to_file(self):
        f = open('zipcodes', "x")
        for zip in self.zip_codes:
            f.write(f"{zip} \n")
        f.close()


get_zips = Jobs()
get_zips.save_to_file()
get_zips.driver.close()