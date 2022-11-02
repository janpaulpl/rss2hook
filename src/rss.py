from post import Embed
import feedparser


class Feed:
    '''Type for RSS feed.'''

    def __init__(self, url: str, name: str, old_embeds: set[Embed], regex="*"):
        self.url = url
        self.name = name
        self.old_embeds = old_embeds
        self.regex = regex

    def __init__(self, feed: dict):
        '''Construct Feed from servers.json formatted feed.'''
        old_embeds = set()  # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
        self.__init__(feed["url"], feed["name"],
                      old_embeds, feed.get("regex", "*"))

    def embeds(self, url: str) -> set[Embed]:
        '''Set of Embeds at url'''
        feed_text = feedparser.parse(url)
        try:
            embeds = {{"title": e.title,
                       "description": f"[{e.description}]({e.link})"} for e in feed_text.entries}
        except AttributeError:
            embeds = {{"title": e.title,
                       "description": e.description} for e in feed_text.entries}
        return embeds

    def updates(self) -> set[Embed]:
        '''Set of Embeds currently in Feed not in old_embeds'''
        return self.embeds().difference(self.old_embeds())
