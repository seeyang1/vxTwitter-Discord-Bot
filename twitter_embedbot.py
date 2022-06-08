#bot that will send twitter links with embedded images/videos
#developed by Brandon Giang 3/16/2022

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
    #------------------------------------------------------------------------    
    if message.author == client.user: #checking to see if the message is sent by the bot itself
        return
    else:
        x = re.split("\s",message.content)
        if twitterCheck(x):
            for words in x: #to go through the message that was sent 
                if "vxtwitter" in words: #this means the fix has already been applied so no need to do anything
                    return
                if "twitter.com" in words: #found twitter link
                    newLink = words.replace("twitter","c.vxtwitter") #replaces twitter with vx twitter
                else:
                    usrMsg=usrMsg+words+" " # here just in case somebody sends text alongside the twitter link
            await message.delete() # work flow: delete original message -> send the fixed media message(s)
            await message.channel.send(message.author.display_name+": "+usrMsg+'\n'+newLink)
            #message format: 
            #{usr}: [usrMsg] newLink
            # [Other pictures if applicable]
            return 
        else:
            return

client.run('Token')