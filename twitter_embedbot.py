#bot that will send twitter links with embedded images/videos
#developed by Brandon Giang 3/16/2022

from asyncio.windows_events import NULL
from audioop import mul
from queue import Empty
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
    multiEmbedFlg=False #if flag is false, the link only has 1 image/embed
    newLink=""
    usrMsg=""
    embedArr=message.embeds #to detect multiple embeds  
    linkArr=[] #for when multiEmbedFlg is true
    txtFlg=False #flag to check if the tweet is purely text
#------------------------------------------------------------------------

#this message parsing:
    x = re.split("\s",message.content)
    for words in x: #to go through the message that was sent 
        if "vxtwitter" in words: #this means the fix has already been applied so no need to do anything
            return
        if "twitter.com" in words: #found twitter link
            tweetFlag = True
            newLink = words.replace("twitter","vxtwitter") #replaces twitter with vx twitter
            if len(embedArr) > 1: #to check if there's more than one embed meaning there's multiple pictures
                multiEmbedFlg = True
                for i in embedArr:
                    linkArr.append(i.image.url)
                linkArr[0]=newLink # to make the first link that's sent the vxtwitter link
        else:
            usrMsg=usrMsg+words+" "
    if tweetFlag:
        await message.delete()
        if multiEmbedFlg:
            await message.channel.send(message.author.display_name+": "+usrMsg+linkArr[0])
            for i in range(1,len(embedArr)):
                await message.channel.send(str(i+1)+"/"+str(len(embedArr)))
                await message.channel.send(linkArr[i])
        else:
            await message.channel.send(message.author.display_name+": "+usrMsg+'\n'+newLink)
            #delete message from the usr who sent twitter link 
            #message format:
            #{usr} said [usrMsg] \n newLink
    else:
        return

client.run('token')

