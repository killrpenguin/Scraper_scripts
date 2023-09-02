from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from selenium import webdriver
from selenium.webdriver import EdgeOptions

def web_driver(*, proxy):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless'),
    edge_options.add_argument('disable-gpu')
    edge_options.add_argument("--proxy_server=%s" % proxy)
    driver = selenium.webdriver.Edge(options=edge_options)
    return driver


def populate_card_info(card_name, proxy):
    xpath_card_name = "/html/body/div[3]/div[1]/div/div[3]/h1/span[1]"
    xpath_card_type = "/html/body/div[3]/div[1]/div/div[3]/p[1]"
    xpath_cmc = "/html/body/div[3]/div[1]/div/div[3]/h1/span[2]/abbr"
    xpath_legal_status = "/html/body/div[3]/div[1]/div/div[3]/dl/div[6]/div[1]"
    xpath_card_text = "/html/body/div[3]/div[1]/div/div[3]/div"
    pause = randint(5, 12)
    driver = web_driver(proxy=proxy)
    driver.get('https://scryfall.com/')
    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=pause, poll_frequency=.8, ignored_exceptions=errors)
    search_box = driver.find_element(By.XPATH, "//html/body/div[@id='main']//div[@class='homepage']"
                                                    "//div[@class='inner-flex']//form[@class='homepage-form']"
                                                    "//input[@id='q']")
    search_box.send_keys(card_name)
    search_box.send_keys(Keys.ENTER)
    card_name = wait.until(ec.presence_of_element_located((By.XPATH, xpath_card_name))).text
    card_type = wait.until(ec.presence_of_element_located((By.XPATH, xpath_card_type))).text
    cmc = wait.until(ec.presence_of_element_located((By.XPATH, xpath_cmc))).text
    legal_status = wait.until(ec.presence_of_element_located((By.XPATH, xpath_legal_status))).text
    card_text = wait.until(ec.presence_of_element_located((By.XPATH, xpath_card_text))).text
    driver.close()