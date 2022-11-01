import feedparser
import json

NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
entry = NewsFeed.entries[1]

print(entry.keys())

# [Dynamically updating JSON](https://stackoverflow.com/questions/52073574/dynamic-json-in-python)
# data = {"mainkey": "val1", "key2": list()}

# # Parse CSV file
# df1 = pd.read_csv(path, header=None)
# # iterate through csv
# for row,s in df1.iterrows():
#     number = df1.loc[row,0]

#     # I'm reading keyb and keyc values from CSV as well, 
#     # but for brevity my substitution below is not showing that.... 
#     data['key2'].append({
#         "keya":number,
#         "keyb":"whatever",
#         "keyc":"whatever",
#     })

site = {
  "YCombinator" : 
  {
    "url": "https://news.ycombinator.com/rss",
    "user": "",
    "title": ""
  }
}

json_object = json.dumps(site, indent=2)
 
# Writing to feeds.json
with open("../data/feeds.json", "w") as outfile:
    outfile.write(json_object)