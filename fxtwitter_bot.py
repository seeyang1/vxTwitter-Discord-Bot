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

#-----------------needed variables---------------------------------------
    tweetFlag=False #if flag is false, usr didn't send a twitter link
    newLink=""
    usrMsg=""
#------------------------------------------------------------------------

#Check for video embed here:

#this message parsing:
    x = re.split("\s",message.content)
    for words in x: #to go through the message that was sent 
        if "fxtwitter" in words: #this means the fix has already been applied so no need to do anything
            return
        if "twitter" in words:
            tweetFlag=True
            newLink = words.replace("twitter","vxtwitter")
            #usrMsg=usrMsg+"[Twitter link] "
        else:
            usrMsg=usrMsg+words+" "
    if tweetFlag:
        await message.delete()
        await message.channel.send(message.author.mention+": "+usrMsg+newLink)
        #delete message from the usr who sent twitter link 
        #message format:
        #@{usr} said [usrMsg] \n newLink


client.run('Token')
