# step 1 importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# step 2 loading the data from csv file using pandas
df = pd.read_csv('netflix_data.csv')
print(df.head())

# step 3 cleaning the Data => Handling missing values, Remove duplicates and fixing columns if needed
df = df.dropna(subset = ['type','release_year','rating','country','duration'])

# movies vs tv shows (counting unique values from type, column using vale_count() func as it will count total num of movies and tv shows)
type_counts = df['type'].value_counts()

# making a barchart from above data
plt.figure(figsize = (6, 4))
plt.bar(type_counts.index, type_counts.values, color = ['skyblue','orange'])
plt.title('Number of Movies Vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

# how much the rating of content distributed in piechart
rating_counts = df['rating'].value_counts()
'''
plt.figure(figsize = (20,14))
plt.pie(rating_counts , labels = rating_counts.index  , autopct = '%1.1f%%', startangle = 90)
plt.title('Percentage of content rating')
plt.tight_layout()
plt.savefig('content_rating.png')
plt.show()
'''

# Combine smaller categories
top_ratings = rating_counts.nlargest(5)  # top 5 categories
others = rating_counts.iloc[5:].sum()
rating_simplified = pd.concat([top_ratings, pd.Series({'Others': others})])
plt.figure(figsize=(8, 6))
plt.pie(rating_simplified, labels=rating_simplified.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Rating (Grouped)')
plt.tight_layout()
plt.savefig('content_rating.png')
plt.show()

# making the histogram

movie_df = df[df['type'] == 'Movie'].copy() #filtering only movies
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)
'''
This line extracts numeric values from the “duration” column.
Let's say the “duration” column looks like:
148 min
195 min
90 min
Here's what happens step by step:
.str.replace('min','') → removes the word "min"
→ "148 min" → "148"
.astype(int) → converts the strings into integers
→ "148" → 148
So you get a new column:
duration	duration_int
148 min	148
195 min	195
90 min	90

This prepares numeric data for plotting.

'''

plt.figure(figsize = (8,6))
plt.hist(movie_df['duration_int'], bins = 30, color = 'lightblue', edgecolor = 'gray')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.xlabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png')
plt.show()


# Scatterplot to check relationship between release year and number of shows

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize = (10,6))
plt.scatter(release_counts.index, release_counts.values, color ='red') # .values gives ypou only value not index or row, column name
plt.title('Relation between release year and number of shows')
plt.xlabel('Release year')
plt.xlabel('Number of shows')
plt.tight_layout()
plt.savefig('release_year_scatterplot.png')
plt.show()

# Top ten countries that have most numbers of movies and shows

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize = (8,6))
plt.barh(country_counts.index, country_counts.values, color = 'teal')
plt.title('Top ten countries by number of movies and shows')
plt.xlabel('Number of shows')
plt.ylabel('Number of countries')
plt.tight_layout()
plt.savefig('barh_plot_of_top_ten_countries.png')
plt.show()

# How many or total number of shows and movies are released in specific year
release_year_count = df['release_year'].value_counts()
plt.figure(figsize = (8,6))
plt.bar(release_year_count.index, release_year_count.values, color = 'black')
plt.title('Years in which how many movies and shows are released')
plt.xlabel('Number of Years')
plt.ylabel('Number of Shows and movies')
plt.tight_layout()
plt.savefig('barh_plot_year_release.png')
plt.show()



content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig , ax = plt.subplots(1,2, figsize = (12,5))
# first Subplot
ax[0].plot(content_by_year.index, content_by_year['Movie'], color = 'blue')
ax[0].set_title('Movies Release per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# second Subplot
ax[0].plot(content_by_year.index, content_by_year['TV Show'], color = 'yellow')
ax[0].set_title('TV Shows Release per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

fig.suptitle('Comparison of movies and TV shows released over years')
plt.tight_layout()
plt.savefig('movies_tvshow_comparison.png')
plt.show()