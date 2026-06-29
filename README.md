# Activity Log Analyzer

## Purpose
Activity Log Analyzer is a Python command-line tool that analyzes CSV-based activity logs and generates summary statistics about activity frequency and consistency.

## Features
- Reads activity logs from a CSV file.
- Calculates total entries.
- Counts unique activities.
- Reports the most common activity.
- Counts the number of active days.
- Handles malformed input files gracefully.
- Written in Python using the standard libraries collections, sys, and csv.

## Input Format
The filename can be specified (default is "log.csv"), with error checking in case the file is missing, cannot be opened, or if the formatting is wrong. Blank lines will be skipped. It should start with the headings for the columns/entries. Each line should be the date (format not specified, though it should be the same for all dates so it can be checked for repetition), the activity, and any notes on the activity (not required). At present, this mostly uses the activities, with the exception of checking how many dates have activities. Including the CSV file in the folder is sufficient. 

## Example Usage
Create a CSV file such as:

```csv
date,activity,note
2026-01-01,reading,
2026-01-01,coding,worked on lists

2026-01-02,coding,fixed bug
2026-01-02,puzzle,crossword
```

Run the program with:
```bash
python activity_log_analyzer.py log.csv
```

## Example Output
```text
Total entries: 4
Unique activities: 3
Most common activity: coding (2)
Days with entries: 2
```

## Future Improvements
- Add date parsing to report the first and last recorded dates and the overall date range.
- Report the frequency of all activities, sorted from most to least common.
- Compute consistency metrics such as the longest activity streak, inactive days, and average entries per active day.
