from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.gitapi import reqUser
from bleach import linkify


#setting webdriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#creating driver
driver = webdriver.Chrome(options=options)

def getLinks(login):
    chars, name, location = reqUser(login)
    #parameters = "Information Technology & Services Internet Computer Software"

    driver.get('http://www.google.com/')

    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys(f"{name} {location} linkedin")
    search_bar.send_keys(Keys.RETURN)

    driver.current_url
    
    users = driver.find_elements_by_partial_link_text(f"{name}")

    links = []
    for u in users:
        links.append(u.get_attribute('href'))

    return {n:d for n,d in enumerate(links)}