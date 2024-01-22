# Final_project_cs50_data_preprocessing
## Overview
The purpose of this project is to process Twitter data stored in a CSV file, extract relevant information, and perform preprocessing steps to create a new dataset. The Python script, process_tweets.py, contains functions for importing data, extracting hashtags, editing usernames, handling missing values, integrating the dataset, and exporting the preprocessed data to a new CSV file.

## Project Workflow:
Data Import: The script begins by importing the Twitter data from a CSV file using the import_data function.

Processing Steps: The data undergoes a series of processing steps, including hashtag extraction, username editing, and handling missing values, carried out by various specialized functions.

Integration: The processed information is integrated into a new DataFrame using the integrate_df function.

Export: The original and preprocessed dataset columns are printed, and the preprocessed data is exported to a new CSV file using the export_as_csv function.

![Alt Text](https://github.com/Fairpart/Final_project_cs50_data_preprocessing/raw/main/image/flow_chart.png)

### Files and Functions
![Alt Text](https://github.com/Fairpart/Final_project_cs50_data_preprocessing/blob/main/image/flow_chart.png)
1. process_tweets.py
This is the main script that orchestrates the entire data processing pipeline. The main() function serves as the entry point, prompting the user to input the location of the data file. It then calls various functions to import, process, and export the data.

Functions:
  - import_data(data_loc): Reads the CSV file using pandas and returns a DataFrame.
  - split_out_hashtags(df): Extracts hashtags from the tweet content and separates them into lists.
  - username_edit(df): Edits and extracts information from the usernames column.
  - handle_missing_and_none(df): Handles missing or invalid numeric values in specified columns.
  - integrate_df(df, hashtag_ls, content_without_hashtags, username_ls): Integrates the processed information into a new DataFrame.
  - export_as_csv(df, new_df): Prints the original and preprocessed dataset columns and exports the new dataset to a CSV file.

2. Data for experiment
In this repository there are two csv files include : Full Data.csv and test_set.csv. Full_data is bigger than test_set.csv I provide these data for someone who Interesting for implementing Thai sentiment analysis or text classification task.
