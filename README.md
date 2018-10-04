TelegramMessageBot
====================================

TelegramMessageBot is a project to send a message from a bot to a Telegram chat. The script was written and tested in Python 3.7.

[![Build status](https://ci.appveyor.com/api/projects/status/aguev1q9qr3en4dd?svg=true)](https://ci.appveyor.com/project/SeppPenner/telegrammessagebot)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/TelegramMessageBot.svg)](https://github.com/SeppPenner/TelegramMessageBot/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/TelegramMessageBot.svg)](https://github.com/SeppPenner/TelegramMessageBot/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/TelegramMessageBot.svg)](https://github.com/SeppPenner/TelegramMessageBot/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/TelegramMessageBot/master/License.txt)

# Steps to use this project:
1. Make sure to install Python and Pip correctly
2. Set the execute flags:

```bash
chmod +x run.sh
```

3. Install all required pip package dependencies with:

```bash
pip install -r requirements.txt
```

4. Adjust your settings in the [bot.py](https://github.com/SeppPenner/TelegramMessageBot/blob/master/bot.py) file (Get your bot token from https://core.telegram.org/bots):

```python
botToken = 'YourBotToken' # Change to your bot token
chatId = '12345' # Change to your chat id
```

5. Run the project using:
```bash
./run.sh
```

or with

```bash
python bot.py
```

# For more information see:
* https://medium.com/@xabaras/sending-a-message-to-a-telegram-channel-the-easy-way-eb0a0b32968
* https://core.telegram.org/bots/api
* https://core.telegram.org/bots

Change history
--------------

* **Version 1.0.0.0 (2018-10-04)** : 1.0 release.
