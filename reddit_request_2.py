"""And thank you for the offer to put something together for me! That's so kind and I should have come back to the
thread earlier! Yes, it's for work and FWIW the website I want to scrape is

johnlewis.com (British department store)
and I want to grab the category and sub category for a given product link. They both sit inside the <ol> tag for the
breadcrumb trail. If you have any specific tips given that extra info I'd love to hear them!"""
import time

from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from seleniumwire.webdriver import EdgeOptions


class Driver_Adapter(webdriver.Edge):
    def __init__(self, link, *args, **kwargs):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("start-maximized")
        edge_options.page_load_strategy = "eager"
        edge_options.add_argument("disable-gpu")
        # edge_options.add_argument("headless")
        edge_options.add_argument("--proxy_server=%s" % "http://24.158.29.166:80")
        super().__init__(edge_options=edge_options)
        self.link = link
        self.valid_resps = [200, 301, 302, 307, 404]
        self.get(self.link)
        self.h2 = self.get_h2
        self.sub_catagories = self.get_data

    @property
    def get_h2(self) -> str:
        h2_xpath = '//*[@id="nav"]/ul/li[1]/h2'
        wait = WebDriverWait(self, 30)
        self.h2 = wait.until(ec.presence_of_element_located((By.XPATH, h2_xpath))).text
        return self.h2

    @property
    def get_data(self) -> dict:
        sub_catagories_xpath = '//*[@id="nav"]/ul/li[1]/ul/descendant::a'
        wait = WebDriverWait(self, 30)
        catagories_links = wait.until(ec.presence_of_all_elements_located((By.XPATH, sub_catagories_xpath)))
        self.sub_catagories = {attribute.text: attribute.get_attribute("href") for attribute in catagories_links}
        return self.sub_catagories


with open("pages", "r") as all_links:
    with open("scraped_data", "x") as scraped_data:
        page_links = all_links.read().strip().split('\n')
        for page_link in page_links:
            scraper = Driver_Adapter(link=page_link)
            scraped_data.write(f"{scraper.h2}\n")
            for (key, value) in zip(scraper.sub_catagories.keys(), scraper.sub_catagories.values()):
                scraped_data.write(f'\t{key},{value}\n')
            scraped_data.write(f'\n')
