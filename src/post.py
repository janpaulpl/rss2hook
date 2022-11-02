from rss import Feed
from discordwebhook import Discord
import requests
import json


class Embed:
    '''Discord formatted embed'''

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def discord_payload(self) -> dict:
        '''Format as Discord payload,'''
        return {"title": self.title, "description": self.description}

    def slack_payload(self) -> dict:
        '''Format as Slack payload.'''
        return set()


class Post:
    '''Discord formatted post'''

    def __init__(self, username: str, embeds: list[Embed], avatar_url="https://raw.githubusercontent.com/jpVinnie/discord-rss-hook/main/data/rss.jpeg"):
        self.username = username
        self.embeds = embeds
        self.avatar_url = avatar_url

    def post_discord(self, url: str) -> None:
        '''Post self to discord webhook at url.'''
        webhook = Discord(url=url)
        webhook.post(
            username=self.username,
            avatar_url=self.avatar_url,
            embed=[e.discord_payload() for e in self.embeds])

    def post_slack(self, url: str) -> None:
        '''Post self to slack webhook at url.'''
        for e in self.embeds:
            requests.post(url, e.slack_payload)


class Channel:
    '''Channel representing single webhook and feeds'''

    def __init__(self, hook_url: str, name: str, feeds: set[Feed], type: str):
        assert type in ["discord", "slack"]
        self.hook_url = hook_url
        self.name = name
        self.feeds = feeds
        self.type = type

    def __init__(self, ch: dict):
        '''Construct Channel from servers.json formatted channel dictionary.'''
        feeds = {Feed(f) for f in ch["feeds"]}
        self.__init__(ch["webhook url"], ch["name"], feeds, ch["type"])

    def process(self):
        '''Get and post updates for every feed in channel.'''
        for feed in self.feeds:
            try:
                embeds = feed.updates()
                # TODO TODO TODO TODO TODO Add avatar
                post = [Post(feed.name, embeds) for e in embeds]
                if self.type == "discord":
                    post.post_discord(self.hook_url)
                else:
                    post.post_slack(self.hook_url)

            except Exception as e:
                print(
                    f"Exception with:\n    channel= {self.name}\n    feed= {feed.name}\n{e}")
