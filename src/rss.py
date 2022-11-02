import feedparser
import ssl
import pprint


class Embed:
    '''Discord formatted embed'''

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def slack_payload(self) -> dict:
        '''Format as Slack payload.'''
        return set()


class Feed:
    '''Type for RSS feed.'''

    def __init__(self, feed: dict):
        '''Construct Feed from servers.json formatted feed.'''
        old_embeds = set()  # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

        self.url = feed["url"]
        self.name = feed["name"]
        self.old_embeds = old_embeds
        self.regex = feed.get("regex", "*")

    def embeds(self) -> set[Embed]:
        '''Set of Embeds at url'''
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        feed_text = feedparser.parse(self.url)
        if feed_text["bozo"] == 1:
            raise feed_text.bozo_exception
        try:
            embeds = {Embed(title=e.title, description=f"[{e.description}]({e.link})")
                      for e in feed_text.entries}
        except AttributeError:
            embeds = {Embed(title=e.title, description=e.description)
                      for e in feed_text.entries}
        return embeds

    def updates(self) -> set[Embed]:
        '''Set of Embeds currently in Feed not in old_embeds'''
        return self.embeds().difference(self.old_embeds)
