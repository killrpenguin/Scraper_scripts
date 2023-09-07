import re
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from selenium.webdriver import EdgeOptions


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
        wait = WebDriverWait(self.driver, 15)
        zips = wait.until(ec.presence_of_element_located((By.XPATH, zips_xpath))).text.split('\n')
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
print(get_zips.zip_codes)
get_zips.driver.close()