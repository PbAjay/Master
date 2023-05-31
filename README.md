<p align="center">
  <img src="assets/logo.jpg" alt="Logo">
</p>
<h1 align="center">
  <b>ᴍᴀꜱᴛᴇʀ</b>
</h1>


[![Stars](https://img.shields.io/github/stars/PbAjay/Master?style=flat-square&color=yellow)](https://github.com/PbAjay/Master/stargazers)
[![Forks](https://img.shields.io/github/forks/PbAjay/Master?style=flat-square&color=orange)](https://github.com/PbAjay/Master/fork)
[![Size](https://img.shields.io/github/repo-size/PbAjay/Master?style=flat-square&color=green)](https://github.com/PbAjay/Master/)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/PbAjay/Master)   
[![Contributors](https://img.shields.io/github/contributors/PbAjay/Master?style=flat-square&color=green)](https://github.com/PbAjay/Master/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/PbAjay/Master/blob/V3/LICENSE)
[![Sparkline](https://stars.medv.io/PbAjay/Master.svg)](https://stars.medv.io/PbAjay/Master)


## Features

- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store
## Variables


### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* Check [info.py](https://github.com/PbAjay/Master/blob/V3/info.py) for more


## Deploy
You can deploy this bot anywhere.

<i>**[Watch Deploying Tutorial...](https://youtu.be/1G1XwEOnxxo)**</i>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PbAjay/Master)

<details><summary>Deploy To Render</summary>
<br>
<a href="https://render.com/deploy?repo=https://github.com/PbAjay/Master/tree/web">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/PbAjay/Master
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Commands
```
logs - to get the rescent errors
stats - to get status of files in db.
filter - add manual filters
filters - view filters
connect - connect to PM.
disconnect - disconnect from PM
del - delete a filter
delall - delete all filters
deleteall - delete all index(autofilter)
delete - delete a specific file from index.
info - get user info
id - get tg ids.
imdb - fetch info from imdb.
users - to get list of my users and ids.
chats - to get list of the my chats and ids 
index  - to add files from a channel
leave  - to leave from a chat.
disable  -  do disable a chat.
enable - re-enable chat.
ban  - to ban a user.
unban  - to unban a user.
channel - to get list of total connected channels
broadcast - to broadcast a message to all Master users
batch - to create link for multiple posts
link - to create link for one post
```


## Thanks to 
 - Base Repo [EvaMaria](https://github.com/EvaMariaTG/EvaMaria)
 - Some Feature [PROFESSOR-BOT](https://github.com/MrMKN/PROFESSOR-BOT)
 - OpenAI Feature [Annaben](https://github.com/Lalluss/annaben_2.35)
 - Thanks To All 
 - Thanks To All 
 - 
