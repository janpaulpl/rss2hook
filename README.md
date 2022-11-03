# RSS feed for Slack/Discord channel webhooks

## Set up
Before starting a local instance, run the following script to add the necessary files/folders

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
              "avatar": "online host: ./data/private/img/rss.jpeg",
              "old items": "./data/private/old_items/nature.json"
            }
          ]
        }
      ]
    }
  ]
}
```

**Scuffed Warning:** We recommend for the `avatar` field to use an image-hosting site because Discord only allows for publicly hosted images for the webhook avatar. (something like imgur should work fine)

### Feedback
Feel free to open an issue with any doubts or suggestions!
 I will never be able to write git push`