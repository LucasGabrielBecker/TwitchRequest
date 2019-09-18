import requests, json
import pandas as pd
import matplotlib.pyplot as plt

url = "https://wind-bow.glitch.me/twitch-api/channels/freecodecamp"
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent= 5, sort_keys=True)


channels = ["ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "storbeck", "habathcx", "RobotCaleb", "noobs2ninjas",
            "ninja", "shroud", "Dakotaz", "esltv_cs", "pokimane", "tsm_bjergsen", "boxbox", "wtcn", "a_seagull",
            "kinggothalion", "amazhs", "jahrein", "thenadeshot", "sivhd", "kingrichard", "tfue"]

channels_list = []
for channel in channels:
    JSONContent = requests.get("https://wind-bow.glitch.me/twitch-api/channels/" + channel).json()
    if 'error' not in JSONContent:
        channels_list.append([

        JSONContent['_id'],
        JSONContent['display_name'],
        JSONContent['status'],
        JSONContent['followers'],
        JSONContent['views'],
        JSONContent['url'],
        JSONContent['language']
        ])



dataset = pd.DataFrame(channels_list)
dataset.columns = ['id', 'Name', 'Status', 'Followers', 'Views', 'URL', 'Language']
dataset.dropna(axis = 0, how= 'any', inplace=True)
dataset.index = pd.RangeIndex(len(dataset.index))
dataset.to_csv('twitchRequest.csv', ',')

x = dataset['Name']
y = dataset['Followers']

plt.bar(x, y, align='center', alpha=0.5)

plt.title('TWITCH REQUEST')
plt.xlabel('Channel Name', rotation=90)
plt.ylabel('Number of Followers')
plt.xticks(rotation=90)

plt.show()



