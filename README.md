# Discord RSS feed Webhook
RSS feed webhook for Discord servers.

## Back-end configuration

- JSON with all channels listed 
- ...

## TODO
We have to check if the content is the same before posting, if so do we 
  - Retry to load and find if the content changes (What makes content change, how long do we wait?)
  - Skip and don't send a message
  - A combination of both?

### References
[How to use RSS](https://cyber.harvard.edu/rss/rss.html)
[Feedparser docs](https://github.com/kurtmckee/feedparser)
[Discord webhook docs](https://github.com/10mohi6/discord-webhook-python)