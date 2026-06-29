from collections import Counter
import csv
import sys

def get_path(argv):
    if argv:
        f = argv[0]
    else:
        f = "log.csv"
    return f

def read_records_csv(f):
    try:
        with open(f, "r", newline="") as file:
            csvreader = csv.reader(file)
            next(csvreader)
            records = [(row[0], row[1], " ".join(row[2:])) for row in csvreader if row] #note is rendered without commas
            return records
    except FileNotFoundError:
        return None

def compute_stats(records):
    activities = [activity for (_date, activity, _note) in records]
    counts = Counter(activities)
    d = {}
    d["total_entries"] = len(records)
    d["unique_activities"] = len(counts)
    d["most_common_activity"], d["most_common_count"] = counts.most_common(1)[0]
    dates = [date for (date, _activity, _note) in records]
    d["days_with_entries"] = len(set(dates))
    return d

def print_stats(d):
    print(f"Total entries: {d['total_entries']}")
    print(f"Unique activities: {d['unique_activities']}")
    print(f"Most common activity: {d['most_common_activity']} ({d['most_common_count']})")
    print(f"Days with entries: {d['days_with_entries']}")
    return 0

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    path = get_path(argv)
    records = read_records_csv(path)
    if records is None:
        print(f"{path} does not exist")
        return 1
    stats = compute_stats(records)
    print_stats(stats)

     
if __name__ == "__main__":
    raise SystemExit(main())