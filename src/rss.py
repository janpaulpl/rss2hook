import feedparser
import ssl
import json


class Feed:
    '''Type for RSS feed.'''

    def __init__(self, feed: dict):
        '''Construct Feed from servers.json formatted feed.'''

        self.url = feed["url"]
        self.name = feed["name"]
        self.old_items_file = feed["old items"]
        self.avatar = feed["avatar"]
        self.regex = feed.get("regex", "*")

    def items(self) -> list[str]:
        '''Set of items at url'''
        # Create SSl context
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        # Parse feed, raise error if parsing incomplete
        feed_text = feedparser.parse(self.url)
        if feed_text["bozo"] == 1:
            raise feed_text.bozo_exception

        # Try to parse entries
        try:
            embeds = {f"[{e.title}]({e.link})" for e in feed_text.entries}
        except AttributeError:
            embeds = {e.title for e in feed_text.entries}

        return embeds

    def updates(self) -> list[str]:
        '''Set of Embeds currently in Feed not in old_embeds'''
        f = open(self.old_items_file, "r")
        o = json.load(f)["old items"]
        f.close()

        return list(set(self.items()).difference(set(o)))

    def save_old(self, old_items: list[str]) -> None:
        '''Save list of items to self.old_items_file json.'''
        f = open(self.old_items_file, "w")
        json.dump({"old items": old_items}, f)
        f.close()
