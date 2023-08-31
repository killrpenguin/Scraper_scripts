from selenium.webdriver.support import expected_conditions as ec
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


table = """//html[@id='​']//body//div[@id='root']//div[@class='sn-182o7r0 sn-1q4qxi9']//div//div[@class='sn-token-provider ⚙ a0 a1 a2 a3 ⚙1qnohcy']
//div[@class='Shell Shell-loaded Sidebar--expanded sn-token-provider ⚙ t0 a4 a5 ⚙gnvn1p']
//div[@class='Shell-container Box-root Flex-flex']//div[@class='Box-root'][2]//div[@class='Content Box-root']
//div[@class='Content-container Box-root']
//div[@class='Content-articleContainer sn-token-provider ⚙ r5 r6 t1 a45 a46 a47 a48 a49 a4a a4b a4c a4 a4d ⚙lk3vj4']
//div[@class='Box-root Flex-flex Flex-direction--row']//div[@class='Content-article MarkdocContentWrapper Box-root']
//article[@id='content']//div[@class='Document']//div[@class='TabGroup TabGroup--tabs Box-root']
//div[@class='ControlledContentGroup-content']//span/div[@class='TabGroup-Tab Box-root']
//div[@class='TabGroup TabGroup--tabs Box-root']//div[@class='ControlledContentGroup-content']
//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--drop-down Box-root'][1]
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']
//div[@class='Table Table--striped ⚙ r5 r6 rl a19 a20 a1x a4e a4f a4g a4h a4i a4j a4k a4l a4m a4n a4o ⚙1bms2uy']"""
routing = """//html[@id='​']//body//div[@id='root']//div[@class='sn-182o7r0 sn-1q4qxi9']//div//div[@class='sn-token-provider ⚙ a0 a1 a2 a3 ⚙1qnohcy']
//div[@class='Shell Shell-loaded Sidebar--expanded sn-token-provider ⚙ t0 a4 a5 ⚙gnvn1p']
//div[@class='Shell-container Box-root Flex-flex']/div[@class='Box-root'][2]
//div[@class='Content Box-root']/div[@class='Content-container Box-root']
//div[@class='Content-articleContainer sn-token-provider ⚙ r5 r6 t1 a45 a46 a47 a48 a49 a4a a4b a4c a4 a4d ⚙lk3vj4']
//div[@class='Box-root Flex-flex Flex-direction--row']
//div[@class='Content-article MarkdocContentWrapper Box-root']//article[@id='content']//div[@class='Document']
//div[@class='TabGroup TabGroup--tabs Box-root']//div[@class='ControlledContentGroup-content']
//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--tabs Box-root']
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--drop-down Box-root'][1]
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']
//div[@class='Table Table--striped ⚙ r5 r6 rl a19 a20 a1x a4e a4f a4g a4h a4i a4j a4k a4l a4m a4n a4o ⚙1bms2uy']
//table[@class='⚙ a4p a4q a4r a4s a4h a4i a4t a35 ⚙g4azxi']
//tbody//tr[@class='⚙ a4u ⚙2mu81k'][1]
//td[@class='⚙ r5 r6 a4w a3n a3o a21 a2i a3p a3q a1y a2j a57 a1b a58 a59 a5a ⚙733xbh'][1]"""
account = """//html[@id='​']//body//div[@id='root']//div[@class='sn-182o7r0 sn-1q4qxi9']//div//div[@class='sn-token-provider ⚙ a0 a1 a2 a3 ⚙1qnohcy']
//div[@class='Shell Shell-loaded Sidebar--expanded sn-token-provider ⚙ t0 a4 a5 ⚙gnvn1p']
//div[@class='Shell-container Box-root Flex-flex']/div[@class='Box-root'][2]
//div[@class='Content Box-root']/div[@class='Content-container Box-root']
//div[@class='Content-articleContainer sn-token-provider ⚙ r5 r6 t1 a45 a46 a47 a48 a49 a4a a4b a4c a4 a4d ⚙lk3vj4']
//div[@class='Box-root Flex-flex Flex-direction--row']
//div[@class='Content-article MarkdocContentWrapper Box-root']//article[@id='content']//div[@class='Document']
//div[@class='TabGroup TabGroup--tabs Box-root']//div[@class='ControlledContentGroup-content']
//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--tabs Box-root']
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--drop-down Box-root'][1]
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']
//div[@class='Table Table--striped ⚙ r5 r6 rl a19 a20 a1x a4e a4f a4g a4h a4i a4j a4k a4l a4m a4n a4o ⚙1bms2uy']
//table[@class='⚙ a4p a4q a4r a4s a4h a4i a4t a35 ⚙g4azxi']
//tbody//tr[@class='⚙ a4u ⚙2mu81k'][2]
//td[@class='⚙ r5 r6 a4w a3n a3o a21 a2i a3p a3q a1y a2j a57 a1b a58 a59 a5a ⚙733xbh'][1]"""
routing_equals = """//html[@id='​']//body//div[@id='root']//div[@class='sn-182o7r0 sn-1q4qxi9']//div//div[@class='sn-token-provider ⚙ a0 a1 a2 a3 ⚙1qnohcy']
//div[@class='Shell Shell-loaded Sidebar--expanded sn-token-provider ⚙ t0 a4 a5 ⚙gnvn1p']
//div[@class='Shell-container Box-root Flex-flex']/div[@class='Box-root'][2]
//div[@class='Content Box-root']/div[@class='Content-container Box-root']
//div[@class='Content-articleContainer sn-token-provider ⚙ r5 r6 t1 a45 a46 a47 a48 a49 a4a a4b a4c a4 a4d ⚙lk3vj4']
//div[@class='Box-root Flex-flex Flex-direction--row']
//div[@class='Content-article MarkdocContentWrapper Box-root']//article[@id='content']//div[@class='Document']
//div[@class='TabGroup TabGroup--tabs Box-root']//div[@class='ControlledContentGroup-content']
//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--tabs Box-root']
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--drop-down Box-root'][1]
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']
//div[@class='Table Table--striped ⚙ r5 r6 rl a19 a20 a1x a4e a4f a4g a4h a4i a4j a4k a4l a4m a4n a4o ⚙1bms2uy']
//table[@class='⚙ a4p a4q a4r a4s a4h a4i a4t a35 ⚙g4azxi']
//tbody//tr[@class='⚙ a4u ⚙2mu81k'][1]
//td[@class='⚙ r5 r6 a4w a3n a3o a21 a2i a3p a3q a1y a2j a57 a1b a58 a59 a5a ⚙733xbh'][2]"""
account_equals = """//html[@id='​']//body//div[@id='root']//div[@class='sn-182o7r0 sn-1q4qxi9']//div//div[@class='sn-token-provider ⚙ a0 a1 a2 a3 ⚙1qnohcy']
//div[@class='Shell Shell-loaded Sidebar--expanded sn-token-provider ⚙ t0 a4 a5 ⚙gnvn1p']
//div[@class='Shell-container Box-root Flex-flex']/div[@class='Box-root'][2]
//div[@class='Content Box-root']/div[@class='Content-container Box-root']
//div[@class='Content-articleContainer sn-token-provider ⚙ r5 r6 t1 a45 a46 a47 a48 a49 a4a a4b a4c a4 a4d ⚙lk3vj4']
//div[@class='Box-root Flex-flex Flex-direction--row']
//div[@class='Content-article MarkdocContentWrapper Box-root']//article[@id='content']//div[@class='Document']
//div[@class='TabGroup TabGroup--tabs Box-root']//div[@class='ControlledContentGroup-content']
//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--tabs Box-root']
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']//div[@class='TabGroup TabGroup--drop-down Box-root'][1]
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']
//div[@class='Table Table--striped ⚙ r5 r6 rl a19 a20 a1x a4e a4f a4g a4h a4i a4j a4k a4l a4m a4n a4o ⚙1bms2uy']
//table[@class='⚙ a4p a4q a4r a4s a4h a4i a4t a35 ⚙g4azxi']
//tbody//tr[@class='⚙ a4u ⚙2mu81k'][2]
//td[@class='⚙ r5 r6 a4w a3n a3o a21 a2i a3p a3q a1y a2j a57 a1b a58 a59 a5a ⚙733xbh'][2]"""
dropdown_xpath = """//html[@id='​']//body//div[@id='root']//div[@class='sn-182o7r0 sn-1q4qxi9']
//div//div[@class='sn-token-provider ⚙ a0 a1 a2 a3 ⚙1qnohcy']
//div[@class='Shell Shell-loaded Sidebar--expanded sn-token-provider ⚙ t0 a4 a5 ⚙gnvn1p']
//div[@class='Shell-container Box-root Flex-flex']
//div[@class='Box-root'][2]//div[@class='Content Box-root']
//div[@class='Content-container Box-root']
//div[@class='Content-articleContainer sn-token-provider ⚙ r5 r6 t1 a45 a46 a47 a48 a49 a4a a4b a4c a4 a4d ⚙lk3vj4']
//div[@class='Box-root Flex-flex Flex-direction--row']//div[@class='Content-article MarkdocContentWrapper Box-root']
//article[@id='content']//div[@class='Document']//div[@class='TabGroup TabGroup--tabs Box-root']
//div[@class='ControlledContentGroup-content']//span//div[@class='TabGroup-Tab Box-root']
//div[@class='TabGroup TabGroup--tabs Box-root']//div[@class='ControlledContentGroup-content']//span
//div[@class='TabGroup-Tab Box-root']
//div[@class='TabGroup TabGroup--drop-down Box-root'][1]
//label//div[@class='DropDownSelector Box-root Box-divider--light-bottom-1 Flex-flex Flex-alignItems--center']
//div[@class='Box-root Flex-flex Flex-alignItems--baseline Flex-direction--row']
//div[@class='Box-root Flex-flex Flex-alignItems--baseline Flex-direction--row Flex-justifyContent--flexStart']
//div[@class='DropDownSelector--Group Box-root']
//div[@class='Box-root Flex-flex Flex-alignItems--baseline Flex-direction--row Flex-justifyContent--flexStart Flex-wrap--nowrap']
//div[@class='Box-root Box-hideIfEmpty']
//div[@class='PressableCore PressableCore--cursor--pointer PressableCore--height--medium PressableCore--radius--all PressableCore--width PressableCore--width--auto PressableButton Select Select--size--medium Box-root Flex-inlineFlex']
//div[@class='PressableCore-base Box-root']//select[@id='Select11']"""
proxy = 'http://45.225.184.177:999'
edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument("--proxy_server=%s" % proxy)
driver = selenium.webdriver.Edge(options=edge_options)
driver.get("https://stripe.com/docs/connect/payouts-bank-accounts?bank-account-collection-method=manual-entry&bank-account-collection-integration=direct-api")
element = driver.find_element(By.XPATH, dropdown_xpath)
select = Select(element)
options_list = select.options
options_list = [option.text for option in options_list]

print(options_list)
element.send_keys("a")

for dd_opt in options_list:
    driver.implicitly_wait(2)
    try:
        target_element = driver.find_elements(By.XPATH, table)
        table_data = [data.text for data in target_element]
        table_data = [string.split('\n') for string in table_data]
        table_data = [a for a in table_data[0]]
        table_data.pop(0)
        table_data = [data.strip() for data in table_data]
        print(dd_opt)
        table_data = [print('\t' + data) for data in table_data]
        element.send_keys(Keys.ARROW_DOWN)
        driver.implicitly_wait(2)
    except UnicodeEncodeError:
        pass
f.close()
driver.close()
