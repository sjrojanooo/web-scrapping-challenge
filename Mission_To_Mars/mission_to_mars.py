#!/usr/bin/env python
# coding: utf-8

# In[66]:


#Dependencies
import os 
import pandas as pd
import numpy as py
import pymongo
import requests
from splinter import Broweser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


# In[20]:


# URL of page to be scrapped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[21]:


#Retrieve page with requests module
response = requests.get(url)


# In[22]:


#Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[23]:


#Examining the results, then determine element that contains sought info
print(soup.prettify())


# In[24]:


# results are returned as an iterable list
titles = soup.find_all('div', class_= 'content_title')

print(titles)


# NASA MARS NEWS

# In[25]:


paragraphs = soup.find_all('div', class_='rollover_description')

print(paragraphs)


# In[26]:


#Storing title and paragraphs into variables for later use
title = 'NASA to Broadcast Mars 2020 Perseverance Launch, Prelaunch Activities'

paragaphs = 'Starting July 27, news activities will cover everything from mission engineering and science to returning samples from Mars to, of course, the launch itself.'


# In[28]:


results = soup.find_all('div',class_='slide')


# In[47]:


#We can also accomplish the same task by returning the results in an iterable list
for result in results:
    #error handling
    try: 
        #Identity and return title of listing
        the_titles = result.find('div', class_='content_title')
        
        #Return the title text 
        title = the_titles.find('a').text
        
        #Identify and return price of listing
        bodies = result.find('div', class_='rollover_description')
        
        #Identify and return link to listing
        body_text = bodies.find('div',class_='rollover_description_inner').text
        
        #Pring results only if title, price, and link are available
        if(title and bodies):
            print('-------------------------------------------------------------------------------')
            print(f'\nTitle:\n{title}')
            print(f'\nBody:\n{body_text}')
    except AttributeError as e:
        print(e)
        


# JPL MARS SPACE IMAGES -FEATURED IMAGE 

# In[51]:


#Address of url to be scraped
url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

#Retrieve page with requests module
response = requests.get(url)

#Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[53]:


#print(soup.prettify())


# In[55]:


#pulling images from website
images = soup.find_all('a',class_='fancybox')


# In[57]:


#print(images)


# In[63]:


#for loop to iterate through images 
image_png = []

for image in images:

    png = image['data-fancybox-href']
        
    image_png.append(png)
        
image_url = 'https://www.jpl.nasa.gov' + png
    
image_url


# MARS FACTS

# In[69]:


#url address to scrape mars facts
mars_url = 'https://space-facts.com/mars/'

#putting information into a table 
table = pd.read_html(mars_url)

#displaying hmtl output
table[0]


# In[71]:


#create a pandas dataframe for the table
mars_facts_df = pd.DataFrame(table[0])

#renaming columns 
mars_facts_df.columns = ['Facts','Value']

#setting index to facts
mars_facts_df.set_index = ['Facts']

#displaying dataframe
mars_facts_df


# In[74]:


#converting data into an html table string
html_facts = mars_facts_df.to_html()

#replacing next line command with a blank space
html_facts = html_facts.replace('\n','')

#presenting the html string
html_facts 


# MARS HEMISPHERES

# CERBERUS ENHANCED HEMISPHERE

# In[146]:


#Scrapping the cerberus hemisphere url
cerebrus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

response = requests.get(cerebrus_url)

soup = bs(response.text, 'html.parser')


# In[147]:


#print(soup.prettify())


# In[148]:


#obtaining the high resolution url for cerberus image
cerberus_img = soup.find_all('div', class_ ='wide-image-wrapper')

print(cerberus_img)


# In[149]:


#iterate through the cerberus img 
for image in cerberus_img: 
    cerberus_image = image.find('li')
    full_cerberus_image = cerberus_image.find('a')['href']
    print(f'\n{full_cerberus_image}\n')
        
cerberus_title = soup.find('h2', class_ = 'title').text
print(f'\n{cerberus_title}\n')

cerberus_hemisphere = {'Title': cerberus_title, 'URL':full_cerberus_image}
print(f'\n{cerberus_hemisphere}\n')


# SCHIAPARELLI HEMISPHERE ENHANCED

# In[150]:


#Scrapping the schiaparelli hemisphere url
schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

response = requests.get(schiaparelli_url)

soup = bs(response.text, 'html.parser')

#print(soup.prettify())


# In[151]:


shiaparelli_img = soup.find_all('div', class_ = 'wide-image-wrapper')

print(shiaparelli_img)


# In[152]:


#iterate through the shiaparelli img
for image in shiaparelli_img:
    shiaparelli_image = image.find('li')
    full_shiaparelli_image = shiaparelli_image.find('a')['href']
    print(f'\n{full_shiaparelli_image}\n')

shiaparelli_title = soup.find('h2', class_ = 'title').text
print(f'\n{shiaparelli_title}\n')

shiaparelli_hemisphere = {'Title': shiaparelli_title, 'URL':full_shiaparelli_image}
print(f'\n{shiaparelli_hemisphere}\n')


# SYRTIS MAJOR HEMISPHERE ENHANCED

# In[153]:


syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

response = requests.get(syrtis_url)

soup = bs(response.text, 'html.parser')

#print(soup.prettify())


# In[154]:


syrtis_image = soup.find_all('div', class_ = 'wide-image-wrapper')

print(syrtis_image)


# In[155]:


#iterate through the syrtis img web page
for image in syrtis_image: 
    syrtis_image = image.find('li')
    full_syrtis_image = syrtis_image.find('a')['href']
    print(f'\n{full_syrtis_image}\n')
    
syrtis_title = soup.find('h2', class_ = 'title').text
print(f'\n{syrtis_title}\n')

syrtis_hemisphere = {'Title': syrtis_title, 'URL':full_syrtis_image}
print(f'\n{syrtis_hemisphere}\n')
    


# VALLES MARINERIS HEMISPHERE ENHANCED

# In[156]:


valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

response = requests.get(valles_url)

soup = bs(response.text, 'html.parser')

#print(soup.prettify())


# In[157]:


valles_img = soup.find_all('div',class_='wide-image-wrapper')

print(valles_img)


# In[158]:


#iterate through the image url
for image in valles_img:
    valles_image = image.find('li')
    full_valles_image = valles_image.find('a')['href']
    print(f'\n{full_valles_image}\n')
    
valles_title = soup.find('h2', class_='title').text
print(f'\n{valles_title}\n')

valles_hemisphere = {'Title': valles_title, 'URL':full_valles_image}
print(f'\n{valles_hemisphere}\n')

