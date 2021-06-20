# What is this?

This is a simple Discord Bot coded in Python that uses the free CryptoCompare API to display cryptocurrency prices
[![Discord Crypto Bot](https://github.com/kevintr303/Discord_Crypto_Bot/blob/main/screenshots/$cb_command.png?raw=true)](#Installation)

## Download

Use git to clone the repository or just download it as a ZIP

```bash
git clone https://github.com/kevintr303/Discord_Crypto_Bot
```

## Installation

The only external Python libraries that are needed are:

```bash
pip3 install discord.py
pip3 install cryptocompare
```
Next, [create your bot on Discord](https://discord.com/developers/applications).
Afterwards, you need to set the environment variables. 
* Set "CRYPTOCOMPARE_API_KEY" to your CryptoCompare api key which you can get [here](https://min-api.cryptocompare.com/) for free (100k calls monthly, 250k cap). 
* Next, set "TOKEN" to your Discord Bot's token.

## Usage
In the [script](https://github.com/kevintr303/Discord_Crypto_Bot/blob/main/bot.py), there are some simple settings you can change:

```python3
# Settings:
base_command = "$cb"
bot_channel = "crypto_tracker"
# End of settings--
```
The **base_command** variable is the command people will use for the bot, and **bot_channel** is the name of the channel where the bot works. The main command of the bot: `$cb` will show all the current commands that exist. For ease I will also list the commands here: **(make sure to have exact capitalization and formatting)**
1. `$gb` lists information and commands
2. `$gb [coin] [currency]` Usage: `$gb BTC USD` Shows current price of a coin
3. `$gb history [coin] [currency] [date]` Usage: `$gb history BTC USD 2021/6/20` Shows historical price of a coin
4. `$gb coins` Links to the CryptoCompare website that shows all coin types

## Why did I make this?
Well, mostly for fun and as a learning experience. I wanted to create something that might be useful and thought, "hey, bitcoin's pretty popular right now. I should make a discord bot that tells you the current price," And so I did. This also marks my very first repository on GitHub(and first Discord bot). At the time of writing this, I have been learning Python for about 4-5 months now, so the code isn't the greatest.

## What did I learn?
From this, I learned about **environment variables** and how to use them, how to create **discord bots**, and **event handling using Python decorators**. That's a win if you ask me, to future projects we go! (Although I might revisit this in the future to improve on my code!)

## License
[MIT](https://choosealicense.com/licenses/mit/)
