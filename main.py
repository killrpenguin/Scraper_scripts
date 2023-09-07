from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from header_practice import Card
import re

def web_driver(*, proxy):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless'),
    edge_options.add_argument('disable-gpu')
    edge_options.add_argument("--proxy_server=%s" % proxy)
    driver = selenium.webdriver.Edge(options=edge_options)
    return driver

link = "https://www.moxfield.com/decks/HYT9YcG0bEK1UMvmEEXtTA"
proxy = 'http://24.158.29.166:80'
deck_xpath = '//*[@id="maincontent"]/div[8]/div[1]/div[2]/div[1]'
driver = web_driver(proxy=proxy)
driver.get(link)
wait = WebDriverWait(driver, 20)

class test_target():
    def __init__(self, driver):
        self.decklist = wait.until(ec.presence_of_element_located((By.XPATH, deck_xpath))).text.split('\n')
        self.card_list = self.clean_decklist(self.decklist)

    def clean_decklist(self, deck):
        # regex replaces all numbers, and the 9 card type catagories from each list with ''
        deck = [
            re.sub("^[0-9]|^[0-9][0-9]|^C.+(.)|^A.+(.)|^E.+(.)|^B.+(.)|^P.+(.)|^I.+(.)|^S.+(.)|^L.+(.)", '', card) for
            card in self.decklist]
        deck = [card.strip() for card in self.decklist if '' != card if '$' not in card]
        for item in deck:
            print(item)
            self.decklist.append(Card(item))



deck = test_target(driver=driver)
for i in range(len(deck.card_list)):
    print(f"{deck.card_list[i].card_name}, {deck.card_list.faces[i].card_type}")