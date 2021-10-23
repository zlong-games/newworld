import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def most_recent_notes(*args):
    chromeOptions = Options()
    chromeOptions.headless = True
    browser = webdriver.Chrome(
        executable_path="./drivers/chromedriver", options=chromeOptions)
    browser.get("https://www.newworld.com/en-us/news?tag=updates")
    nameList = browser.find_elements_by_class_name(
        'ags-SlotModule-spacer')[0]
    nameList.click()
    for option in args:
        if option == "url":
            url = browser.current_url

        elif option == "title":
            title = browser.find_element_by_class_name(
                'ags-NewsArticlePage-contentWrapper-articlePane-articleTitle').text

        elif option == "desc":
            desc = browser.find_elements_by_class_name(
                'ags-rich-text-div')[0].text
            desc = (f"{desc[:200]}...")
        elif option == "date":
            date = browser.find_element_by_class_name(
                "ags-NewsArticlePage-contentWrapper-articlePane-blogDate").text
        elif option == "img":
            img = browser.find_element_by_class_name(
                "ags-MediaGalleryEmbed-container-gallery-box-thumbnail-image").get_attribute('src')
        else:
            continue
    browser.quit()
    return url, title, desc, date, img
