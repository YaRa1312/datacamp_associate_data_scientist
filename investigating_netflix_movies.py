# **Netflix**! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.
# 
# Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.
# 
# You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!
# 
# You have been supplied with the dataset `netflix_data.csv`, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!
# 
# ## The data
# ### **netflix_data.csv**
# | Column | Description |
# |--------|-------------|
# | `show_id` | The ID of the show |
# | `type` | Type of show |
# | `title` | Title of the show |
# | `director` | Director of the show |
# | `cast` | Cast of the show |
# | `country` | Country of origin |
# | `date_added` | Date added to Netflix |
# | `release_year` | Year of Netflix release |
# | `duration` | Duration of the show in minutes |
# | `description` | Description of the show |
# | `genre` | Show genre |

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
# the most frequent movie duration in the 1990s

all_1990_movies_durations = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999) & (netflix_df['type'] == 'Movie')]['duration'].to_list()
series = pd.Series(all_1990_movies_durations)
duration = series.value_counts().idxmax()
print(duration)

# the number of short action movies

short_movie_count = 0

for label, row in netflix_df.iterrows():
    if row['release_year'] >= 1990 and row['release_year'] < 2000 and row['type'] == 'Movie' and row['genre'] == 'Action' and row['duration'] < 90:
        short_movie_count += 1
                
print(short_movie_count)
