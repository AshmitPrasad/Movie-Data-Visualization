#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Supress Warnings

import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Import the numpy and pandas packages

import numpy as np
import pandas as pd


# In[3]:


import os 
print(os.listdir())


#  

# ## Reading and Inspection
# 
# -  ###  Import and read
# 
# Import and read the movie database. Store it in a variable called `movies`.

# In[4]:


movies =pd.read_csv('Movie.csv') # Write your code for importing the csv file here
movies


# -  ###  Inspect the dataframe
# 
# Inspect the dataframe's columns, shapes, variable types etc.

# In[5]:


# Write your code for inspection here
movies.info()


# ##  Cleaning the Data
# 
# -  ###  Inspect Null values
# 
# 
# Find out the number of Null values in all the columns and rows. Also, find the percentage of Null values in each column. Round off the percentages upto two decimal places.

# In[6]:


# Write your code for column-wise null count here
#method 1 
movies.isnull().sum()


# In[7]:


#method 2
movies.isna().sum()


# In[8]:


# Write your code for row-wise null count here
 # method 1
movies.isna().sum(axis = 1)


# In[9]:


movies.isnull().sum(axis = 1)


# In[10]:


#3rd way to get result
for i in range(len(movies.index)):
    print('NaN values in row',i,':',movies.iloc[i].isna().sum())


# In[11]:


# Write your code for column-wise null percentage
perc = perc =(movies.isna().sum() * 100)/len(movies)
perc


# In[12]:


perc =(movies.isna().sum() * 100)/len(movies)
perc


# -  ###  Drop unecessary columns
# 
# For this assignment, you will mostly be analyzing the movies with respect to the ratings, gross collection, popularity of movies, etc. So many of the columns in this dataframe are not required. So it is advised to drop the following columns.
# -  color
# -  director_facebook_likes
# -  actor_1_facebook_likes
# -  actor_2_facebook_likes
# -  actor_3_facebook_likes
# -  actor_2_name
# -  cast_total_facebook_likes
# -  actor_3_name
# -  duration
# -  facenumber_in_poster
# -  content_rating
# -  country
# -  movie_imdb_link
# -  aspect_ratio
# -  plot_keywords

# In[13]:


# Write your code for dropping the columns here. It is advised to keep inspecting the dataframe after each set of operations 
dropcoluns = ['color','director_facebook_likes','actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes',
             'actor_2_name','cast_total_facebook_likes','actor_3_name','duration','facenumber_in_poster','content_rating',
             'country','movie_imdb_link','aspect_ratio','plot_keywords']
for i in dropcoluns:
    movies.drop([i],axis=1,inplace= True)
movies.info()    


# In[ ]:





# -  ###  Drop unecessary rows using columns with high Null percentages
# 
# Now, on inspection you might notice that some columns have large percentage (greater than 5%) of Null values. Drop all the rows which have Null values for such columns.

# In[14]:


# Write your code for dropping the rows here

selectedcolumns = ['gross','budget']
for i in selectedcolumns:
    movies.dropna(subset=selectedcolumns,how='any',inplace=True)


# In[15]:


perc =(movies.isna().sum() * 100)/len(movies)
perc


# -  ###  Drop unecessary rows
# 
# Some of the rows might have greater than five NaN values. Such rows aren't of much use for the analysis and hence, should be removed.

# In[16]:


# Write your code for dropping the rows here
for i in range(len(movies.index)):
    s= movies.iloc[i].isna().sum()
    if s>5:
        movies.drop(i,axis = 0,inplace=True)
movies.isna().sum(axis = 1)


# In[ ]:





# -  ###  Fill NaN values
# 
# You might notice that the `language` column has some NaN values. Here, on inspection, you will see that it is safe to replace all the missing values with `'English'`.

# In[17]:


# Write your code for filling the NaN values in the 'language' column here
movies.fillna(value='language',axis=1,inplace=True)
movies['language']


# -  ###  Check the number of retained rows
# 
# You might notice that two of the columns viz. `num_critic_for_reviews` and `actor_1_name` have small percentages of NaN values left. You can let these columns as it is for now. Check the number and percentage of the rows retained after completing all the tasks above.

# In[18]:


# Write your code for checking number of retained rows here
movies.isna().sum(axis =1)
print( round(100*len(movies.index)/5043,2))


# **Checkpoint 1:** You might have noticed that we still have around `77%` of the rows!

# ##  Data Analysis
# 
# -  ###  Change the unit of columns
# 
# Converting the unit of the `budget` and `gross` columns from `$` to `million $`.

# In[19]:


# Write your code for unit conversion here
movies['budget'].apply(lambda x:x/1000000)
movies['gross'].apply(lambda x:x/1000000)


# -  ###  Find the movies with highest profit
# 
#     1. Create a new column called `profit` which contains the difference of the two columns: `gross` and `budget`.
#     2. Sort the dataframe using the `profit` column as reference.
#     3. Extract the top ten profiting movies in descending order and store them in a new dataframe - `top10`

# In[20]:


# Write your code for creating the profit column here
movies['PROFIT']=movies['gross']-movies['budget']
movies.head()


# In[21]:


# Write your code for sorting the dataframe here
movies.sort_values(by='PROFIT',ascending=False)


# In[22]:


# Write your code to get the top 10 profiting movies here
top10 = movies.head(10)
top10


# -  ###  Drop duplicate values
# 
# After you found out the top 10 profiting movies, you might have notice a duplicate value. So, it seems like the dataframe has duplicate values as well. Drop the duplicate values from the dataframe and repeat `Subtask 3.2`.

# In[23]:


# Write your code for dropping duplicate values here
movies.drop_duplicates()


# In[24]:


# Write code for repeating subtask 2 here
top10 = movies.head(10)
top10


#  You might spot two movies directed by `James Cameron` in the list.

# 

# In[25]:


# Write your code for extracting the top 250 movies as per the IMDb score here. Make sure that you store it in a new dataframe 
# and name that dataframe as 'IMDb_Top_250'
IMDb_Top_250=movies.sort_values(by='imdb_score',ascending=False)
IMDb_Top_250


# In[26]:


Top_Foreign_Lang_Film =IMDb_Top_250[IMDb_Top_250.language!='English']
Top_Foreign_Lang_Film# Write your code to extract top foreign language films from 'IMDb_Top_250' here


# You can  spot `Veer-Zaara` in the dataframe

# - ###  Find the best directors
# 
#     1. Group the dataframe using the `director_name` column.
#     2. Find out the top 10 directors for whom the mean of `imdb_score` is the highest and store them in a new dataframe `top10director`. 

# In[27]:


# Write your code for extracting the top 10 directors here
print(movies.groupby(by='director_name')['imdb_score'].mean().sort_values(ascending = False).head(10))


# No surprises that `Damien Chazelle` (director of Whiplash and La La Land) is in this list.

# -  ###  Find popular genres
# 
# You might have noticed the `genres` column in the dataframe with all the genres of the movies seperated by a pipe (`|`). Out of all the movie genres, the first two are most significant for any film.
# 
# 1. Extract the first two genres from the `genres` column and store them in two new columns: `genre_1` and `genre_2`. Some of the movies might have only one genre. In such cases, extract the single genre into both the columns, i.e. for such movies the `genre_2` will be the same as `genre_1`.
# 2. Group the dataframe using `genre_1` as the primary column and `genre_2` as the secondary column.
# 3. Find out the 5 most popular combo of genres by finding the mean of the gross values using the `gross` column and store them in a new dataframe named `PopGenre`.

# In[28]:


# Write your code for extracting the first two genres of each movie here
genrecollected=movies['genres'].apply(lambda s:pd.Series(s.split('|')))

# genre_1 = genrecollected.iloc[:,0]
# genre_2 = genrecollected[2]
genrecollected
movies['genre_1'] = genrecollected[0]
movies['genre_2'] = genrecollected[1]
print(movies.genre_1)
print(movies.genre_2)


# In[29]:


movies_by_segment =movies.groupby(by=['genre_1','genre_2'])
movies_by_segment# Write your code for grouping the dataframe here


# In[30]:


PopGenre = movies_by_segment['gross'].mean().sort_values(ascending=False).head(5)
PopGenre.head(5)
                                                    # Write your code for getting the 5 most popular combo of genres here


# In[31]:


#method2
PopGenre = movies_by_segment.mean().sort_values(by ='gross',ascending=False).head(5)
PopGenre.head(5)
                    


# In[32]:


movies


#  Well, as it turns out. `Family + Sci-Fi` is the most popular combo of genres out there!

# In[ ]:




