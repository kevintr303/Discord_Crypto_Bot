# Discord Crypto Bot was made by https://github.com/kevintr303 and is under The MIT License

import discord
import os
import cryptocompare
from datetime import datetime

# CryptoCompare API Key needs to be defined here or set up as an environment variable (call it "CRYPTOCOMPARE_API_KEY")
# cryptocompare.cryptocompare._set_api_key_paremeter(KEY_HERE)

# Settings:
base_command = "$cb"
bot_channel = "crypto_tracker"
# End of settings--

client = discord.Client()


# The default message sent if no command parameters are sent
def default_message():
    embed = discord.Embed(title=":sunglasses: Crypto Bot", description="This simple bot tracks several cryptocurrencies using the CryptoCompare API", url="https://github.com/kevintr303", color=0x0fa5f0)
    embed.add_field(name=":money_with_wings: Check Prices", value="```$cb BTC USD```")
    embed.add_field(name=":chart_with_upwards_trend: Check Historical Prices", value="```$cb history ETH EUR 2018,5,20```")
    embed.add_field(name=":coin: Coin List", value="```$cb coins```")
    embed.add_field(name=":warning: NOTE:", value="Minimum date is March 20, 2017", inline=False)
    embed.set_footer(text="made by https://github.com/kevintr303")
    return embed


# Price History Command
def price_history(command, error_message=None, coin=None, currency=None, timestamp=None):
    try:
        coin = command[2]
        currency = command[3]
        date = [int(x) for x in command[4].split(",")]
        timestamp = datetime(date[0], date[1], date[2])
        present = datetime.now()
        if timestamp > present:
            timestamp = present
        # Set the minimum date if older than the minimum date
        elif timestamp < datetime(2017, 3, 20):
            timestamp = datetime(2017, 3, 20)
        return coin, currency, timestamp, error_message
    except IndexError:
        error_message = "**ERROR** Invalid number of parameters."
        return coin, currency, timestamp, error_message
    except ValueError:
        error_message = "**ERROR** Invalid parameters."
        return coin, currency, timestamp, error_message


# Current Price Command
def current_price(command, coin=None, currency=None, error_message=None):
    try:
        coin = command[1]
        currency = command[2]
        return coin, currency, error_message
    except KeyError:
        error_message = "**ERROR** Invalid parameters."
        return coin, currency, error_message


@client.event
async def on_ready():
    print(f"Connected as {client.user}")
    await client.change_presence(activity=discord.Game(name="$cb"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        if message.content == base_command and message.channel.name == bot_channel:
            embed = default_message()
            await message.channel.send(embed=embed)
        else:
            command = message.content.split(" ")
            # Price History Command
            if command[1] == "history":
                coin, currency, timestamp, error_message = price_history(command)
                if error_message:
                    await message.channel.send(error_message)
                try:
                    await message.channel.send(f"{coin} Price @ {timestamp.date()}: **{cryptocompare.get_historical_price(coin, currency, timestamp=timestamp)[coin][currency]} {currency}**")
                except KeyError:
                    await message.channel.send("**ERROR** Invalid parameters.")


            # Coin List Command
            elif command[1] == "coins":
                embed = discord.Embed(title=":coin: Coin List", url="https://www.cryptocompare.com/coins/list/all/USD/1", description="This is a list of valid cryptocurrencies you can use with the bot", color=0x29a347)
                embed.set_thumbnail(url="https://www.cryptocompare.com/media/20567/cc-logo-vert.png")
                await message.channel.send(embed=embed)
            elif command[1] in cryptocompare.get_coin_list(format=True):
                # Current Price Command
                coin, currency, error_message = current_price(command)
                if error_message:
                    await message.channel.send(error_message)
                try:
                    await message.channel.send(f"Current {coin} Price: **{cryptocompare.get_price(coin, currency)[coin][currency]} {currency}**")
                except TypeError:
                    await message.channel.send("**ERROR** Invalid parameters.")
                except KeyError:
                    await message.channel.send("**ERROR** Invalid parameters.")
    # Commands sent in DM
    except AttributeError:
        if isinstance(message.channel, discord.channel.DMChannel):
            pass

if __name__ == "__main__":
    client.run(os.getenv('TOKEN'))  # Place your token here (instead of os.getenv()) or set up an environment variable
