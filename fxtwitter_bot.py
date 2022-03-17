#bot that will send twitter links with embedded images/videos
#developed by Brandon Giang 3/16/2022

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #console output to confirm login

@client.event
async def on_message(message):
    if message.author == client.user: #checking to see if the message is sent by the bot itself
        return

    if message.content.startswith('https://twitter.com/'):

        channel = message.channel
        newLink = message.content.replace("twitter","fxtwitter") #appending fx into the link 
        await message.channel.send(newLink) #sending the link to the the user

client.run('TOKEN HERE')



# to do list: 
# 1) Make the bot be able to read if the twitter link has the twitter link at all
# 2) Have the bot delete the message
#   | Have the bot say who posted the twitter link (prefereably without a ping)
# 
#
#
#
#
# Things to consider:
# Maybe make a flag (ex: make it ![twitter link] symbol not specific)
# if twitfix "failed to scan link " -> display an error message
# Maybe make it so that if someone replies to a message and pings the bot it'll embed twitter link
#
#
#
#
