

#first we need to mount the data from the drive

from google.colab import drive
drive.mount('/content/drive/')

# Commented out IPython magic to ensure Python compatibility.
#let's import the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

file_path = "/content/drive/My Drive/Colab Notebooks/Copy of Airbnb NYC 2019.csv"
airbnb_df = pd.read_csv(file_path)

airbnb_df.shape

#have a look on the columns
airbnb_df.columns

airbnb_df.head()

airbnb_df.tail()

airbnb_df.info()

#lets remove the null values from the data
airbnb_non_null_df = airbnb_df.dropna()

airbnb_non_null_df.info()

airbnb_non_null_df.describe()

#Take the necessary columns only

airbnb_non_null_df = airbnb_non_null_df[['id','name','host_id','host_name','neighbourhood_group','neighbourhood','room_type','price','minimum_nights','number_of_reviews','last_review','reviews_per_month','calculated_host_listings_count','availability_365']]

airbnb_non_null_df.columns

"""# ***Lets explore the hosts and areas***"""

#lets groupby the hosts and areas

host_and_areas = airbnb_non_null_df.groupby(['host_name','neighbourhood_group','neighbourhood'])['calculated_host_listings_count'].count().reset_index()

#lets take the top 5 listing from the data

top_five_host = host_and_areas.sort_values(by='calculated_host_listings_count',ascending= False).head()

top_five_host

plt.bar(top_five_host['host_name'],top_five_host['calculated_host_listings_count'])
plt.show()

"""##  Sonder(NYC) is the host having most no.of listing. John and Vida are in the second and third place for most no.of listing hosts.

"""

neighbourhood_group_count = airbnb_non_null_df['neighbourhood_group'].value_counts()

neighbourhood_group_count

neighbourhood_group_count.plot(kind='pie',autopct="%.2f",figsize=(16,8))
plt.title('Listing of various groups')
plt.show()

"""##**The group Manhattan have the most no.of listing(42.81%)**
##**Group Brooklyn is second in the listing (42.35%)**
##**Staten island have the least no.of listing(0.81%)**

---

# ***Lets explore the reviews among the various locations***
"""

#lets groupby the data

reviews = airbnb_non_null_df.groupby(['name','neighbourhood_group','price'])['number_of_reviews'].sum().reset_index()

reviews.sort_values(by='number_of_reviews',ascending=False)

"""## **Room near JFK Queen Bed is the most reviewed hotel(629).Great Bedroom in Manhattan having the second highest reviewed hotel(607).**

---

## **Reviews amoung various Neighbourhood Groups**
"""

reviews_various_groups = airbnb_non_null_df.groupby(['neighbourhood_group'])['number_of_reviews'].sum().reset_index()

reviews_various_groups

plt.bar(reviews_various_groups['neighbourhood_group'],reviews_various_groups['number_of_reviews'])
plt.show()

"""## **Brooklyn and Manhattan having the most no.of reviews. And staten Island and Bronx having the least no of reviews.**

---

# **Lets explore the price of various hotel**
"""

price1 = reviews.sort_values(by='price',ascending=False)

price1

"""## The **Luxury 1 bedroom apt. -stunning Manhattan views** and **Furnished room in Astoria apartment** are the most costed hotel (**10000**)"""

fig, ax = plt.subplots(figsize=(18, 8))
ax.scatter(x = reviews['price'], y = reviews['number_of_reviews'])
plt.xlabel("price",fontsize=24)
plt.ylabel("reviews",fontsize=24)
plt.title('Price vs Review',fontsize=28)

plt.show()

"""## **In here we can see that most of the people prefers low costed hotels. Also most no.of reviews are came from the hotel having low cost.**

---

# **Busiest Hosts**
"""
#Lets findout the busiest host from the data

busiest_host = airbnb_non_null_df.groupby(['host_name','neighbourhood_group'])['minimum_nights'].count().reset_index()
top_5_busiest_host = busiest_host.sort_values(by='minimum_nights',ascending=False).head()
top_5_busiest_host

name = top_5_busiest_host['host_name']
stayed = top_5_busiest_host['minimum_nights']

fig = plt.figure(figsize=(12,6))
plt.bar(name, stayed, color='red',width=0.5)

plt.xlabel = ('Host Name')
plt.ylabel = ('Minimum Nights')
plt.title = ('Top 5 Busiest Host')
plt.show()

"""## **Sonder (NYC) is the most busiest host (207).Michael(176) and David(149) is in 2nd and 3rd position.**

# ***Traffic among different areas.***
#lets checkout various type of rooms in various neighbourhood group.

various_rooms = airbnb_non_null_df.groupby(['neighbourhood_group','room_type'])['minimum_nights'].count().reset_index()
various_rooms.sort_values(by='minimum_nights',ascending=False)

name = various_rooms['room_type']
stayed = various_rooms['minimum_nights']

fig = plt.figure(figsize=(14,6))
plt.bar(name, stayed, color='green',width=0.5)
plt.show()

## In here we can see that most no.of peoples stayed in **Entire home/apt** and **private room**. Least no.of people prefers **shared room**. So the places having **entire home/apt or private room** is the high traffic area.

## **Average price among various groups.**
