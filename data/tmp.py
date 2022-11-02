import time
from discordwebhook import Discord
import json
import feedparser
# [Dynamically updating JSON](https: // stackoverflow.com/questions/52073574/dynamic-json-in-python)
data = {"mainkey": "val1", "key2": list()}

# Parse CSV file
df1 = pd.read_csv(path, header=None)
# iterate through csv
for row, s in df1.iterrows():
    number = df1.loc[row, 0]

    # I'm reading keyb and keyc values from CSV as well,
    # but for brevity my substitution below is not showing that....
    data['key2'].append({
        "keya": number,
        "keyb": "whatever",
        "keyc": "whatever",
    })


'''Functionality for processing RSS feeds and generating webhook jsons.'''


NewsFeed = feedparser.parse(
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
entry = NewsFeed.entries[1]

print(entry.keys())


json_object = json.dumps(site, indent=2)

# Writing to feeds.json
with open("../data/feeds.json", "w") as outfile:
    outfile.write(json_object)


channels = [
    Discord(url="https://discord.com/api/webhooks/1036990907687374911/oQfMr2EloMMBt6AZ2wTRu__MoeQW1BgXIbYEfsyNZj9i--a5tONPnzqVhzDq3Ay6hgQe"),
    Discord(url="https://discord.com/api/webhooks/1036994009819787295/ovj23eXX4YaJmptZ8KFziWdi2-WRzrYz768P56p6Z7_2h4r1Lylf0_VIMLUwFkZJdPI_")
]

for channel in channels:
    channel.post(
        username="Testing",
        avatar_url="https://avatars2.githubusercontent.com/u/38859131?s=460&amp;v=4",
        embeds=[{"title": "Embed Title", "description": "Embed description"}])
    time.sleep(3)


# from discordwebhook import Discord
# import time

# channels = [
#     Discord(url="https://discord.com/api/webhooks/1036990907687374911/oQfMr2EloMMBt6AZ2wTRu__MoeQW1BgXIbYEfsyNZj9i--a5tONPnzqVhzDq3Ay6hgQe"),
#     Discord(url="https://discord.com/api/webhooks/1036994009819787295/ovj23eXX4YaJmptZ8KFziWdi2-WRzrYz768P56p6Z7_2h4r1Lylf0_VIMLUwFkZJdPI_")
# ]

# for channel in channels:
#     channel.post(
#         username="Testing",
#         avatar_url="https://avatars2.githubusercontent.com/u/38859131?s=460&amp;v=4",
#         embeds=[{"title": "Embed Title", "description": "Embed description"}])
#     time.sleep(3)


def main():
    '''
        For each server S:
        every minutes M:
        For each channel C of S :
        For each RSS R for C :
        Get all new info from R.filter(C)
        Post new info to the discord associated with C
    '''

    # Read servers.json

    # For each server S

    # Every T seconds, format messages
