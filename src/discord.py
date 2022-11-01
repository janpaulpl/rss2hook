from discordwebhook import Discord
import time

# Spec
# For each server:S :
#   every minutes:M :
#   For each channel:C of S :
#   For each RSS:R for C :
#     Get all new info from R.filter(C)
#     Post new info to the discord associated with C

# See servers.json
# {
#   "server1": {
#     "WH-URL": {
#       "RSS-url": ""
#     },
#     "WH-URL2": {
#       "RSS-url": ""
#     }
#   }
# }


channels = [
	Discord(url="https://discord.com/api/webhooks/1036990907687374911/oQfMr2EloMMBt6AZ2wTRu__MoeQW1BgXIbYEfsyNZj9i--a5tONPnzqVhzDq3Ay6hgQe"),
	Discord(url="https://discord.com/api/webhooks/1036994009819787295/ovj23eXX4YaJmptZ8KFziWdi2-WRzrYz768P56p6Z7_2h4r1Lylf0_VIMLUwFkZJdPI_")
	]

for channel in channels:
	channel.post(
		username="Testing",
		avatar_url="https://avatars2.githubusercontent.com/u/38859131?s=460&amp;v=4",
		embeds=[{"title": "Embed Title", "description": "Embed description"}])
	time.sleep(3)