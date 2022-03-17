#bot that will send twitter links with embedded images/videos
#developed by Brandon Giang 3/16/2022

import discord
import re #going to use regex to find twitter link

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #console output to confirm login

@client.event
async def on_message(message):
    if message.author == client.user: #checking to see if the message is sent by the bot itself
        return
    #await message.channel.send(message.content) #debug to see what the bot is seeing
    x = re.search("https://twitter.com",message.content)
    if x == None:
        return
    else:
        channel = message.channel
        newLink = message.content.replace("twitter","fxtwitter") #appending fx into the link 
        await message.channel.send(newLink) #sending the link to the the user

    #if message.content('https://twitter.com/'): #have to find a way to 

        #channel = message.channel
        #newLink = message.content.replace("twitter","fxtwitter") #appending fx into the link 
        #await message.channel.send(newLink) #sending the link to the the user

client.run('TOKEN HERE')

