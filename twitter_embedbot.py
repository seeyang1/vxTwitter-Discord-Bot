#bot that will send twitter links with embedded images/videos
#developed by Brandon Giang 3/16/2022

from asyncio.windows_events import NULL
from audioop import mul
from queue import Empty
import discord
import re 


client = discord.Client()

def twitterCheck(msgArr): #function that takes an array and returns true and false depending on if it contains a twitter link
    #message parsing:           
    for words in msgArr: # finding if a twitter link is sent, should technically be faster if there's no twitter link
        if "twitter.com" in words:
            return True
        else:
            return False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #console output to confirm login

@client.event
async def on_message(message):
    #-----------------needed variables---------------------------------------
    multiEmbedFlg = False #if flag is false, the link only has 1 image/embed
    newLink=""
    usrMsg=""
    embedArr = message.embeds #to detect multiple embeds  
    linkArr=[] #for when multiEmbedFlg is true
    #------------------------------------------------------------------------    
    if message.author == client.user: #checking to see if the message is sent by the bot itself
        return
    else:
        x = re.split("\s",message.content)
        if twitterCheck(x):
            print(message.embeds)
            for words in x: #to go through the message that was sent 
                if "vxtwitter" in words: #this means the fix has already been applied so no need to do anything
                    return
                if "twitter.com" in words: #found twitter link
                    newLink = words.replace("twitter","vxtwitter") #replaces twitter with vx twitter
                    if len(embedArr) > 1: #to check if there's more than one embed meaning there's multiple pictures
                        multiEmbedFlg = True
                        for i in embedArr:
                            linkArr.append(i.image.url)
                        linkArr[0]=newLink # to make the first link that's sent the vxtwitter link
                else:
                    usrMsg=usrMsg+words+" " # here just in case somebody sends text alongside the twitter link
            await message.delete() # work flow: delete original message -> send the fixed media message(s)
            if multiEmbedFlg:
                await message.channel.send(message.author.display_name+": "+usrMsg+linkArr[0])
                for i in range(1,len(embedArr)):
                    progIndicator = str(i+1)+"/"+str(len(embedArr))
                    await message.channel.send(progIndicator+'\n'+linkArr[i])
                return
            else:
                await message.channel.send(message.author.display_name+": "+usrMsg+'\n'+newLink)
                #message format: 
                #{usr}: [usrMsg] newLink
                # [Other pictures if applicable]
                return 
        else:
            return

client.run('token')