if [ ! -d "./data/private" ]
then
    mkdir ./data/private
    mkdir ./data/private/img
    mkdir ./data/private/old_items
    touch ./data/private/old_embeds/old_embeds.json
    touch ./data/private/servers.json
    echo "Private folder instantiated"
else
    echo "Folder already exists"
fi