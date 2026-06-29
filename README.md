## Features
- Reads activity logs from a CSV file.
- Calculates total entries.
- Counts unique activities.
- Reports the most common activity.
- Counts the number of active days.
- Handles malformed input files gracefully.
- Uses the libraries collections, sys, and csv.

## Input Format
The filename can be specified (default is "log.csv"), with error checking in case the file is missing, cannot be opened, or if the formatting is wrong. Blank lines will be skipped. It should start with the headings for the columns/entries. Each line should be the date (format not specified, though it should be the same for all dates so it can be checked for repetition), the activity, and any notes on the activity (not required). At present, this mostly uses the activities, with the exception of checking how many dates have activities. Including the CSV file in the folder is sufficient. 

## Example Usage
date,activity,note
2026-01-01,reading,
2026-01-01,coding,worked on lists

2026-01-02,coding,fixed bug
2026-01-02,puzzle,crossword

python line_analyzer.py log.csv

## Example Output
Total entries: 4
Unique activities: 3
Most common activity: coding (2)
Days with entries: 2

## Future Improvements
Date parsing - first/last dates listed and a total date range
Consistency statistics - listing the most common activities with their frequencies
Streak/consistency statistics - listing the longest streak of days with activities, the number of inactive days in the range, and the average entries per active day