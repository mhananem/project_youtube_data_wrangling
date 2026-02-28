![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)
![logo_ironhack_blue 7](https://logo-marque.com/wp-content/uploads/2020/04/YouTube-Logo.png)
# PROJECT 1 | YouTube Dta Structuring and Wrangling
<details>
  <summary>
   <h2>Project Objectifs</h2>
  </summary>

1. The average engagement rate of videos exceeds 4%.
2. Top channels in terms of views receive the highest number of reactions (+25% compared to average channels).
3. Some categories (e.g., Music/Sport) have a significantly higher number of views compared to other categories.
- The ratio of dislikes to total reactions (likes + dislikes) is similar across categories.
4. Channels with the highest number of subscribers have published the most videos (e.g., gaming channels).
5. Engagement rate decreases overtime.
- Compare the engagement rate of the top 5 videos based on the dataset date versus the API data as of today.



  <br>
  <hr> 

</details>

<details>
  <summary>
   <h2>Context</h2>
  </summary>

Here is the data sources used for this project:

- YouTube data between 2020-2021 mostly using the data for the US and grouped by video_id and channel_id. Source: https://www.kaggle.com/datasets/jashwanthreddya/youtube?resource=download
- YouTube API data fom YouTube API V3. Source: https://developers.google.com/youtube/v3/docs?hl=fr

 
  <br>
  <hr> 

</details>

Description of the documents attached project:

- Youtube_project_structuring_data.ipynb: the python code used for merging, structuring, and visualizing the data.
- functions.py: contains the functions used in the project, mainly for extracting data from the API and performing data cleaning. The functions are stored in a .py file for future reuse.
- video_categories.csv: data by category of video retreived through the API and stored in a .csv file for future reuse.
- channels_data.csv: data by video channel retreived through the API and stored in a .csv file for future reuse.

 
  <br>
  <hr> 

</details>

## Introduction

Key metrics:

- Engagement rate = likes + comments/ number of views
- % Views = Views per channel/ Total Views * 100
- % Reactions = Likes+Comments per channel / Total Reactions * 100 (for % Views vs. % Reactions by Channel)
- % of Total Reactions = Reactions per category/ Total Reactions * 100 (for % of Total Reactions by channel)
- % of Dislikes = Dislikes per category/ Reactions per category * 100 (for % of Dislikes by category)



## Requirements

- Fork this repo
- Clone it to your machine