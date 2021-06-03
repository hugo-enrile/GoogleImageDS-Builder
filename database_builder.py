# -*- coding: utf-8 -*-

"""
Created on Thu Jun 03 13:28:20 2021
@author: hugo.enrile.lacale
@github: hugo-enrile
@email: hugoenrilelacalle@gmail.com
"""

import bs4 as BeautifulSoup
import requests
import zipfile 
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

class Constants():
    """
    A class used to save constants that will be used in the 
    script.

    """

    GOOGLE_PREFIX = "https://www.google.co.in/search?q="
    IMAGE_SUFIX = "&source=lnms&tbm=isch"

class ImageDSBuilder():
    """
    A class used to download images from Google and store them into a zip file
    in order to build an image dataset.

    """

    # Webdriver options for the Selenium library
    webdriver_options = Options()
    webdriver_options.add_argument('--headless')
    webdriver_options.add_argument('--no-sandbox')
    webdriver_options.add_argument('--disable-dev-shm-usage')

    def __init__(self):
        '''
        Initialize the class.

        Returns
        -------
        None.

        '''
        pass

    def select_term(driver, query):
        '''
        Do the search for the input term given by the user.

        Parameters
        ----------
        driver: Selenium
        query: String

        Return
        ------
        BeautifulSoup

        '''

        url_query = Constants.GOOGLE_PREFIX + query + Constants.IMAGE_SUFIX
        driver.get(url_query)
        page_source = driver.page_source
        try:
            html_soup = BeautifulSoup.BeautifulSoup(page_source, 'html.parser')
            return html_soup
        except:
            print("Failed operation, sorry.")
            return None
    
    def download_photos(driver, html_soup, query, path):
        '''
        Creates a folder to store all the images that will be download.

        Parameters
        ----------
        driver: Selenium
        html_soup: BeautifulSoup
        query: String
        path: String

        Return
        ------
        None.

        '''

        new_path = path + "/photos_" + query + "/"
        os.makedirs(new_path)
        photos = html_soup.findAll('img')
        print("Downloading images to photos_" + query + " folder... Please, wait a second.")
        id = 0
        for photo in photos:
            try:
                src = requests.get(photo["src"], allow_redirects=True)
                id = id + 1 
                open(new_path + "photo_" + query + "_" + str(id) + ".jpg", 'wb').write(src.content)
            except:
                try:
                    data_src = requests.get(photo['data-src'], allow_redirects=True)
                    id = id + 1
                    open(new_path + "photo_" + query + "_" + str(id) + ".jpg", 'wb').write(data_src.content)
                except:
                    pass             
    
    if __name__ == '__main__':
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=webdriver_options)
        input_search = input('Introduce what you want to search: ')
        input_path = input("Introduce the path where you want to store the files: ")
        print("Searching " + input_search + "...\n\n")
        html_soup = select_term(driver, input_search)
        download_photos(driver, html_soup, input_search, input_path)
        print("Download finished. Thanks!\n\n")