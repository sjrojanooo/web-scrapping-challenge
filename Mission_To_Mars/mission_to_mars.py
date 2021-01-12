#Dependencies
import os 
import pandas as pd
import numpy as py
import pymongo
import requests
import time
import json
from flask import Flask, render_template
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    #splinter 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    #Mars News Titles
    browser = init_browser()
    mars_collection = {}
    
    #Mars News URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    mars_collection['news_title'] = soup.find('div', class_='content_title').get_text()
    mars_collection['news_snip'] = soup.find('div',class_='rollover_description_inner').get_text()
    
    #Mars Image
    url_image = 'https://www.jpl.nasa.gov/images/?search=&category=Mars'
    browser.visit(url_image)
    response = browser.html
    soup2 = bs(response, 'html.parser')
    images = soup2.find_all('a', class_='fancybox')
    pic_source = []
    for image in images:
        picture = image['data-fancybox-href']
        pic_source.append(picture)
        
    mars_collection['image_url'] = 'https://www.jpl.nasa.gov' + pic_source[2]
    
    #Mars Facts
    url_facts = 'https://space-facts.com/mars/'
    mars_facts_df = pd.read_html(url_facts)[0]
    mars_facts_df.columns = ['Facts','Values']
    clean_table_df = mars_facts_df.set_index(['Facts'])
    mars_table = clean_table_df.to_html()
    mars_table = mars_table.replace('\n','')
    mars_collections['fact_table'] = mars_table
    
    #Mars Hemispheres
    hemisphere_url = [] 
    
    #Cerberus Hemisphere 
    cerberus_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(cerberus_url)
    response_cerberus = browser.html
    soup3 = bs(response_cerberus, 'html.parser')
    cerberus_image = soup3.find_all('div',class_='wide-image-wrapper')
    
    for image in cerberus_image:
        cerberus_img = image.find('li')
        cerberus_full_img = cerberus_img.find('a')['href']
    
    cerberus_title = soup3.find('h2', class_='title').get_text()
    cerberus_hemisphere = {'Title': cerberus_title, 'URL':cerberus_full_img}
    
    hemisphere_url.append(cerberus_hemisphere)
    
    #Shiaparelli Hemisphere
    shiaparelli_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(cerberus_url)
    response_shiaparelli = browser.html
    soup4 = bs(response_shiaparelli, 'html.parser')
    shiaparelli_image = soup4.find_all('div',class_='wide-image-wrapper')
    
    for image in shiaparelli_image:
        shiaparelli_img = image.find('li')
        shiaparelli_full_img = shiaparelli_img.find('a')['href']
    
    shiaparelli_title = soup4.find('h2', class_='title').get_text()
    shiaparelli_hemisphere = {'Title': shiaparelli_title, 'URL':shiaparelli_full_img}
    
    hemisphere_url.append(shiaparelli_hemisphere)
    
    #Syrtis Hemisphere 
    syrtis_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(syrtis_url)
    response_syrtis= browser.html
    soup5 = bs(response_syrtis, 'html.parser')
    syrtis_image = soup5.find_all('div',class_='wide-image-wrapper')
    
    for image in syrtis_image:
        syrtis_img = image.find('li')
        syrtis_full_img = syrtis_img.find('a')['href']
    
    syrtis_title = soup5.find('h2', class_='title').get_text()
    syrtis_hemisphere = {'Title': syrtis_title, 'URL':syrtis_full_img}
    
    hemisphere_url.append(syrtis_hemisphere)
    
    #Valles Hemisphere 
    valles_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(valles_url)
    response_valles = browser.html
    soup6 = bs(response_valles, 'html.parser')
    valles_image = soup6.find_all('div',class_='wide-image-wrapper')
    
    for image in valles_image:
        valles_img = image.find('li')
        valles_full_img = valles_img.find('a')['href']
    
    valles_title = soup6.find('h2', class_='title').get_text()
    valles_hemisphere = {'Title': valles_title, 'URL':valles_full_img}
    
    hemisphere_url.append(valles_hemisphere)
    
    
    #Collection of all the Information
    mars_collection['hemisphere_image'] = hemisphere_url
    
    return mars_collection
    


