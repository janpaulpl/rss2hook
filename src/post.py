from rss import Feed
import requests
import time
import markdownify as md


class Post:
    '''Discord formatted post'''

    def __init__(self, username: str, items: list[str], avatar_url="https://raw.githubusercontent.com/jpVinnie/discord-rss-hook/main/data/rss.jpeg"):
        self.username = username
        self.items = items
        self.avatar_url = avatar_url

    def post_discord(self, url: str) -> None:
        '''Post self to discord webhook at url.'''
        count = 0
        for item in self.items:
            if count != 0:
                time.sleep(3)
            data = {"username": self.username,
                    "avatar_url": self.avatar_url,
                    "content": item}
            result = requests.post(url, data)
            result.raise_for_status()
            count += 1

    def post_slack(self, url: str) -> None:
        '''Post self to slack webhook at url.'''
        count = 0
        for item in self.items:
            data = dict()  # TODO TODO TODO TODO TODO TODO TODO
            result = requests.post(url, data)
            result.raise_for_status()
            if count != 0:
                time.sleep(1)
            count += 1


class Channel:
    '''Channel representing single webhook and feeds'''

    def __init__(self, ch: dict):
        '''Construct Channel from servers.json formatted channel dictionary.'''
        assert ch["type"] in ["discord", "slack"]

        self.hook_url = ch["webhook url"]
        self.name = ch["name"]
        self.feeds = {Feed(f) for f in ch["feeds"]}
        self.type = ch["type"]

    def process(self):
        '''Get and post updates for every feed in channel.'''
        for feed in self.feeds:
            try:
                items = feed.updates()
                post = Post(feed.name, items, avatar_url=feed.avatar)
                if self.type == "discord":
                    post.post_discord(self.hook_url)
                    print(f"posted \nchannel={self.name}\nfeed={feed.name}")
                else:
                    post.post_slack(self.hook_url)
                    print(
                        f"not posted \nchannel={self.name}\nfeed={feed.name}")
                feed.save_old(items)

            except Exception as e:
                print(
                    f"Exception processing\n    channel= {self.name}\n    feed= {feed.name}\n{e}")
