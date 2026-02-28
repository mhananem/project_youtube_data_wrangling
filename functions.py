from googleapiclient.discovery import build
from tqdm import tqdm
import pandas as pd
from  pathlib import Path
import kagglehub

#functions to call the API
##  Extracting the category id for video ids via API and mapping the category ids with category names

def get_category_map(api_key, region_code="US"):
    youtube = build("youtube", "v3", developerKey=api_key)
    
    request = youtube.videoCategories().list(
        part="snippet",
        regionCode=region_code
    )
    response = request.execute()
    
    # Create a mapping of category_id -> category_name
    category_map = {
        cat["id"]: cat["snippet"]["title"] for cat in response.get("items", [])
    }
    return category_map

# to call this function use : df_categories = get_videos_with_category_names(df, API_KEY)

def get_videos_with_category_names(df, api_key, region_code="US"):
    category_map = get_category_map(api_key, region_code)
    
    youtube = build("youtube", "v3", developerKey=api_key)
    
    unique_ids = df["video_id"].dropna().unique().tolist()
    
    results = []
    
    for i in tqdm(range(0, len(unique_ids), 50)):
        batch = unique_ids[i:i+50]
        
        request = youtube.videos().list(
            part="snippet",
            id=",".join(batch)
        )
        response = request.execute()
        
        for item in response.get("items", []):
            category_id = item["snippet"]["categoryId"]
            category_name = category_map.get(category_id, "Unknown")
            
            results.append({
                "video_id": item["id"],
                "category_id": category_id,
                "category_name": category_name
            })
    df_categories = pd.DataFrame(results)
    df_categories.to_csv("video_categories.csv", index=False)  # moved inside the function

    return df_categories



## Extracting the Channels statitics and saving them into a csv file for future use
##to call the function  use : subs_df = get_channel_stats(df, API_KEY)'''

def get_channel_stats(df, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    
    channel_id_list = []
    subs_count_list = []
    videos_count_list = []
    views_count_list = []

    for channel_id in df['channel_id'].unique():
        request = youtube.channels().list(
            part='statistics',
            id=channel_id
        )
        response = request.execute()

        if "items" in response:
            subs = int(response["items"][0]['statistics']['subscriberCount'])
            videos = int(response["items"][0]['statistics']['videoCount'])
            views = int(response["items"][0]['statistics']['viewCount'])
        else:
            subs = None  
            videos = None
            views = None

        channel_id_list.append(channel_id)
        subs_count_list.append(subs)
        videos_count_list.append(videos)
        views_count_list.append(views)

    subs_df = pd.DataFrame({
        "channel_id": channel_id_list,
        "subscriberCount": subs_count_list,
        "viewCount": views_count_list,
        "videoCount": videos_count_list
    })

    subs_df.to_csv("channels_data.csv", index=False)

    return subs_df

#Function to extract uptodate data for tope 5 videos
# to call the functions : 
## top5_videos = df_new.sort_values("engagement_rate", ascending=False).head(5)
## new_video_df = get_top5_stats(top5_videos, API_KEY)
## new_video_df = save_top5(new_video_df, top5_videos)

def get_top5_stats(top5_videos, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)

    video_id_list = []
    new_views_list = []
    new_likes_list = []
    new_comments_list = []

    for video_id in top5_videos["video_id"]:
        request = youtube.videos().list(part="statistics", id=video_id)
        response = request.execute()

        if "items" in response:
            stats = response["items"][0]["statistics"]
            new_views_list.append(int(stats.get("viewCount", 0)))
            new_likes_list.append(int(stats.get("likeCount", 0)))
            new_comments_list.append(int(stats.get("commentCount", 0)))
        else:
            new_views_list.append(None)
            new_likes_list.append(None)
            new_comments_list.append(None)

        video_id_list.append(video_id)

    return pd.DataFrame({
        "video_id": video_id_list,
        "new_views": new_views_list,
        "new_likes": new_likes_list,
        "new_comments": new_comments_list
    })

## map it with video title from top58ideo ( old data dataframe)
def save_top5(new_video_df, top5_videos):
    new_video_df["title"] = new_video_df["video_id"].map(top5_videos.set_index("video_id")["title"])
    new_video_df.to_csv("top5_videos_api.csv", index=False)
    return new_video_df



#Function to download the dataset from Kaggle and loads the first CSV found

def load_data(dataset_slug):
    path = kagglehub.dataset_download(dataset_slug)
    dataset_dir = Path(path)
    csv_path = next(dataset_dir.glob("*.csv"))
    df = pd.read_csv(csv_path)
    return df

# Functions to clean the data in numerical ans categotical columns:
# data_cleaning.py

numerical_cols = ["view_count", "video_count", "subscriber_count", "likes", "dislikes", "comment_count"]

categorical_cols = ["channel_id", "video_id", "title", "channel_title", "tags"]


def standardize_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df


def fill_missing_values(df):
    existing_numerical = [col for col in numerical_cols if col in df.columns]
    existing_categorical = [col for col in categorical_cols if col in df.columns]

    df[existing_numerical] = df[existing_numerical].fillna(
        df[existing_numerical].mean()
    )

    df[existing_categorical] = df[existing_categorical].fillna("Unknown")

    return df


def clean_data(df):
    df = standardize_column_names(df)
    df = fill_missing_values(df)
    return df

def get_channel_titles(df_new):
   #Extract channel titles mapped by channel_id from the main dataframe
    return df_new.drop_duplicates(subset="channel_id").set_index("channel_id")["channel_title"]


def map_channel_titles(channels_df, df_new):
    # Map channel titles onto channels_df using channel_id
    channel_titles = get_channel_titles(df_new)  # was get_channel_titles(df) ← bug
    channels_df["channel_title"] = channels_df["channel_id"].map(channel_titles)
    return channels_df


def drop_missing_counts(channels_df):
    #Drop rows where subscriberCount, viewCount, or videoCount is missing
    return channels_df.dropna(subset=["subscriberCount", "viewCount", "videoCount"])


def convert_to_int(channels_df):
    #Convert viewCount, subscriberCount, and videoCount columns to integers
    for col in ["viewCount", "subscriberCount", "videoCount"]:
        channels_df[col] = channels_df[col].astype(int)
    return channels_df


def drop_duplicate_channels(channels_df):
    #Remove duplicate rows based on channel_id.
    return channels_df.drop_duplicates(subset="channel_id")



