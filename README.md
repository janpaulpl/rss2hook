# RSS feed for Slack/Discord channel webhooks

## Set up
For your local instance, run the following script to add the necessary file structure dependencies

```sh
$ chmod +x build.sh
$ ./build.sh
```

For setting up your own RSS feeds to their corresponding webhooks, [we provide a JSON schema](./data/servers.schema.json). Follow the schema and put your own JSON file in [the private folder](./data/private). Make sure to **never** share your webhook urls or data!

> Example server configuration file

```json
{
  "send frequency": 30,
  "servers": [
    {
      "server id": "serverId",
      "name": "plain text server name",
      "channels": [
        {
          "name": "channel name",
          "type": "discord",
          "webhook url": "WEBHOOK LINK HERE",
          "feeds": [
            {
              "name": "Nature",
              "url": "https://www.nature.com/nature.rss",
              "avatar": "./data/private/img/rss.jpeg",
              "old_embeds": "./data/private/old_embeds/nature.json"
            }
          ]
        }
      ]
    }
  ]
}
```

### Feedback
Feel free to open an issue with any doubts or suggestions!
