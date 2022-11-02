from rss import Feed, Embed
import requests
import json


class Post:
    '''Discord formatted post'''

    def __init__(self, username: str, embeds: list[Embed], avatar_url="https://raw.githubusercontent.com/jpVinnie/discord-rss-hook/main/data/rss.jpeg"):
        self.username = username
        self.embeds = embeds
        self.avatar_url = avatar_url

    def post_discord(self, url: str) -> None:
        '''Post self to discord webhook at url.'''
        for e in self.embeds:
            pass
        data = {"username": self.username,
                "avatar_url": self.avatar_url,
                "content": e.description}
        result = requests.post(url, data)
        result.raise_for_status()

    def post_slack(self, url: str) -> None:
        '''Post self to slack webhook at url.'''
        for e in self.embeds:
            result = requests.post(url, e.slack_payload)
            result.raise_for_status()


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
            # try:
            embeds = feed.updates()
            # TODO TODO TODO TODO TODO Add avatar
            post = Post(feed.name, embeds)
            if self.type == "discord":
                post.post_discord(self.hook_url)
                print(f"posted \nchannel={self.name}\nfeed={feed.name}")
            else:
                post.post_slack(self.hook_url)
                print(
                    f"not posted \nchannel={self.name}\nfeed={feed.name}")

            # except Exception as e:
            #     print(
            #         f"Exception processing\n    channel= {self.name}\n    feed= {feed.name}\n{e}")
