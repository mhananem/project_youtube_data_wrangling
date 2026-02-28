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