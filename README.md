<p align="center">
  <img src="https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png" width="200">
  <img src="https://logo-marque.com/wp-content/uploads/2020/04/YouTube-Logo.png" width="200">
</p>

# PROJECT 1 | YouTube Dta Structuring and Wrangling
<details>
  <summary>
   <h2>Project Objectives</h2>
  </summary>

- Use Python methods to extract and combine data from two different sources with YouTube data.
- Analyze the collected data to validate or reject the hypotheses formulated below.

  <br>
  <hr> 

</details>

<details>
  <summary>
   <h2>Hypotheses</h2>
  </summary>

1. The average engagement rate of videos exceeds 4%.
2. Top channels in terms of views receive the highest number of reactions.
3. Some categories (e.g., Music/Sport) have a significantly higher number of views compared to other categories.
- The ratio of dislikes to total reactions is similar across categories.
4. Channels with the highest number of subscribers have published the most videos.
5. Engagement rate decreases overtime (engagement rate of the top 5 videos based on the dataset date versus the API data as of today).


  <br>
  <hr> 

</details>

<details>
  <summary>
   <h2>Data sources</h2>
  </summary>

The data sources used for this project:

1. YouTube stored data: 
Data between 2020-2021 mostly using the data for the US and grouped by video_id and channel_id. 
Source: https://www.kaggle.com/datasets/jashwanthreddya/youtube?resource=download

2. YouTube API data:
Data fom YouTube API V3. Source: https://developers.google.com/youtube/v3/docs?hl=en

! Important note
How to connect to YouTube API:

✅ Step 1 — Create a Google Cloud Project
1. Go to Google Cloud console: https://console.cloud.google.com/
2. Click Create Project
2. Give a name to your project
3. Click Create

✅ Step 2 — Enable YouTube Data API v3
1. In the left menu → APIs & Services
2. Click Library
3. Search for YouTube Data API v3
4. Click Enable

✅ Step 3 — Create API Key
1. Go to APIs & Services → Credentials
2. Click Create Credentials
3. Select API Key
4. Copy your key (you’ll use it in Python)

✅ Step 4 — Install Python Client
pip install google-api-python-client

✅ Step 5 — Connect in Python
from googleapiclient.discovery import build
API_KEY = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)
print("Connection successful!")

 
  <br>
  <hr> 

</details>

Description of the documents attached to the project:

- Youtube_project_structuring_data.ipynb: the python code used for merging, structuring, and visualizing the data.
- functions.py: contains the functions used in the project, mainly for extracting data from the API and performing data cleaning. The functions are stored in a .py file for future reuse.
- video_categories.csv: data by category of video retreived through the API and stored in a .csv file for future reuse.
- channels_data.csv: data by video channel retreived through the API and stored in a .csv file for future reuse.
- top5_videos_api.csv: data for the top 5 videos (views, kikes, comments) retreived through the API and stored in a .csv file for future reuse.

 
  <br>
  <hr> 

</details>

## Key metrics

- Engagement rate = likes + comments/ number of views
- % Views = Views per channel/ Total Views * 100
- % Reactions = Likes+Comments per channel / Total Reactions * 100 (for % Views vs. % Reactions by Channel)
- % of Total Reactions = Reactions per category/ Total Reactions * 100 (for % of Total Reactions by channel)
- % of Dislikes = Dislikes per category/ Reactions per category * 100 (for % of Dislikes by category)

Link to the presentation with analysis and insights: https://docs.google.com/presentation/d/1UkTDGk2koeg8aSj0KHy8cZFksXwdwWnhQVas0ml0QBk/edit?usp=sharing


## Requirements

- Fork this repo
- Clone it to your machine