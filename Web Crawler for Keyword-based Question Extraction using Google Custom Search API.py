#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Web Crawler for Keyword-based Question Extraction using Google Custom Search API


# In[2]:


# Project Starts 


# In[3]:


import requests     
import pandas as pd        
import json                
from datetime import date, timedelta  


# Global Variables 
questions_list = []

# Get keyword from user
keyword=input("Enter a keyword:")
keyword1=keyword

# Search Keyword on Multiple site
site_list=["quora.com","wikihow.com","thoughtco.com","wikihow.com","reddit.com","brainly.com","wikihow.com","Quora.com","stackexchange.com"]
for site in site_list:
  keyword = keyword + " site:"+ site
  print(keyword)
  

  # Search on Google using Google API's and API'S Key
  
  google_url = " https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyBd0XMJeuOda9cy_N5U8YJlG_GGCqHf0B8&cx=02b10b384370948b4"

  google_url = google_url + "&q=" + keyword
  

  # Sent a network request to google
  response = requests.get(google_url)           

  
  # Convert String Response into JSON Object
  json_response = json.loads(response.text)

    
  total_results = int(json_response["searchInformation"]["totalResults"])


  # Loop through all the responses from google
  total_pages = round(total_results/10)           


  # try-catch block to handle exceptions  
  try:
    # Loop through the responses
    for item in json_response["items"]:
      title = item["title"]
      title = title.replace(" - Quora", "")
      questions_list.append(title)

  except Exception as e:
    print("Exception", e) 


  # Reset the keyword
  keyword = keyword1

  # questions_list
questions_dict = {"Questions": questions_list}
df = pd.DataFrame(data=questions_dict)
df


# In[4]:


# Export the data to a csv file
df.to_csv( keyword1 + "_questions.csv" )


# In[ ]:





# In[ ]:




