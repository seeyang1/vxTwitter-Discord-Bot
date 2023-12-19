#bot that will send twitter links with embedded images/videos
#developed by Brandon Giang 3/16/2022

from hashlib import new
from logging.config import valid_ident
import discord
import re 

intents = discord.Intents.default()
intents.messages=True
intents.message_content=True

client = discord.Client(intents=intents)

def twitterCheck(msgArr): #function that takes an array and returns true and false depending on if it contains a twitter link
    #message parsing:
    print("in the twitter checker")
    print(msgArr)  
    for words in msgArr: # finding if a twitter link is sent, should technically be faster if there's no twitter link
        #print(words)
        if "vxtwitter.com" in words: #this means the fix has already been applied so no need to do anything
            print("found a fix not doing shit")
            return False
        elif "fixvx.com"in words: #this means the fix has already been applied so no need to do anything
            print("found a fix not doing shit")
            return False
        elif "fixupx.com" in words: #this means the fix has already been applied so no need to do anything
            print("found a fix not doing shit")
            return False
        elif "twitter.com" in words:
            print("twitter found\n returning 1")
            return 1
        elif "x.com" in words:
            print("x found\n returning 2")
            return 2
    print("exiting twitter checker, didn't find anything")
    return False

def instagramCheck(msgArr):
    print("in the instagram checker")
    for words in msgArr:
        print("checking for: "+words)
        if "ddinstagram.com" in words:
            return False
        elif "instagram.com" in words: 
            return True
    print("exiting insta checker, nothing found")
    return False

def tiktokCheck(msgArr):
    print("in the tiktok checker")
    for words in msgArr:
        if "vxtiktok.com" in words: 
            return False
        elif "tiktok.com"in words:
            return True
    print("exiting insta checker, nothing found")
    return False
            
def allCheck(msgArr):
    print("In the allCheck funciton")
    print(msgArr)
    if twitterCheck(msgArr):
        print("found a twitter link in using allCheck")
        return True
    elif instagramCheck(msgArr):
        print("found an instagram link using allCheck")
        return True
    elif tiktokCheck(msgArr):
        print("found a tiktok link using allCheck")
        return True
    else:
        return False

def embedFix(msgArr):
    print("in embedFix function")
    usrMsg=""
    newLink=""
    for words in msgArr:
        print("in the for loop in the embedFix")
        print(words)
        if "twitter.com" in words:
            print("yes twitter")
            newLink = words.replace("twitter.com","vxtwitter.com")
            print(newLink)
        elif "x.com" in words:
            print("yes x")
            newLink = words.replace("x.com","fixvx.com") #replaces twitter with vxtwitter for videos
            print(newLink)
        elif "instagram.com" in words:
            print("yes insta")
            newLink = words.replace("instagram","ddinstagram") #replaces twitter with vxtwitter for videos
            print(newLink)
        elif "tiktok.com"in words:
            print("yes tiktok")
            newLink = words.replace("tiktok","vxtiktok") #replaces twitter with vxtwitter for videos
            print(newLink)
        else:
            print("printing usr message variable:")
            usrMsg=usrMsg+" "+words
    print("printing new link and then user message")
    print (newLink)
    print (usrMsg)
    newMsg = usrMsg+" \n"+newLink
    print("printing new message")
    print(newMsg)
    return newMsg

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #console output to confirm login

@client.event
async def on_message(message):
    if message.author == client.user: #checking to see if the message is sent by the bot itself
        return
    else:
        x = re.split("\s",message.content)
        print("parting the red sea")
        print(x)
        if allCheck(x):
            print("in the all check loop")
            await message.delete() # work flow: delete original message -> send the fixed media message(s)
            await message.channel.send(message.author.display_name+":"+embedFix(x))
            #message format: 
            #{usr}: [usrMsg] newLink
            # [Other pictures if applicable]
            return 
        return


client.run('TOKEN')
