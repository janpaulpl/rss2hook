from discordwebhook import Discord

discord = Discord(url="https://discord.com/api/webhooks/1036990907687374911/oQfMr2EloMMBt6AZ2wTRu__MoeQW1BgXIbYEfsyNZj9i--a5tONPnzqVhzDq3Ay6hgQe")
discord.post(content="Hello, world.")