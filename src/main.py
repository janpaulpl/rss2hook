
from discordwebhook import Discord
import feedparser
import json
import time
import urllib
from post import Channel


def main() -> None:
    '''
        For each server s:
        every minutes M:
        For each channel C of s :
        For each RSS R of C :
        Get all new info from R 
        Post new info to the discord associated with C
    '''

    # Read servers.json
    f = open("./data/private/servers.json", 'r')
    data = json.load(f)
    f.close()

    send_freq = data["send frequency"]
    servers = [[Channel(c) for c in s["channels"]]
               for s in data["servers"]]  # Each server is a list of channels

    while True:
        # For each server s, send to each channel
        for s in servers:
            for c in s:
                # Get and post updates for every feed in channel, update last seen embeds
                c.process()
        # Wait send_freq seconds, before sending again
        time.sleep(send_freq)


if __name__ == "__main__":
    main()
