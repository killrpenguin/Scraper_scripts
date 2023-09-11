from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium
import requests
import re
from selenium.webdriver import EdgeOptions



web_link = "https://www.youtube.com/watch?v=rfTgO9rpqck"
proxy = 'http://24.158.29.166:80'
video_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video"

def web_driver(*, proxy):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless'),
    edge_options.add_argument('disable-gpu')
    edge_options.add_argument("--proxy_server=%s" % proxy)
    driver = selenium.webdriver.Edge(options=edge_options)
    return driver

driver = web_driver(proxy=proxy)
driver.get(web_link)
wait = WebDriverWait(driver, 20)
test = wait.until(ec.presence_of_element_located((By.XPATH, video_xpath)))
src = test.get_attribute('src')
clean_link = re.sub("^bl.+:", "", src)
print(clean_link)
driver.get(f"https:{clean_link}")
print(driver.page_source)