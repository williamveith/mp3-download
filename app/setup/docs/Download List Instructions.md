# Create Download List

The download list can be in json for csv. Place the download list in folder Download List. A template download list (CSV with header) has been provided. Feel free to delete these files or use it to create the download list

## JSON

An array of objects. Each object must contain key "url". Keys "title" and "author" are optional & will be assigned default values "untitled" and "unknown" respectively. The file can be named anything. The script will look for the json extension

```json
[
    {
        "url": "https://www.youtube.com/watch?v=QrNti3ZVpYk",
        "title": "Dear Arkansas Daughter",
        "author": "Lady Lamb"
    }
]
```

## CSV

A file containing the url, title, and author on each row. title and author are optional & will be assigned default values "untitled" and "unknown" respectively. A header row can be included or excluded

### With Header

```csv
url,title,author
https://www.youtube.com/watch?v=QrNti3ZVpYk,Dear Arkansas Daughter,Lady Lamb
```

### Without Header

```csv
https://www.youtube.com/watch?v=QrNti3ZVpYk,Dear Arkansas Daughter,Lady Lamb
```
