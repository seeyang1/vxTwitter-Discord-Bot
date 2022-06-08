# vxTwitter-Discord-Bot
A side project utilizing discord.py API and the TwitFix repository


 to do list: 
1) ~~Make the bot be able to read if the twitter link has the twitter link at all (use regex for this)~~
2) ~~Have the bot delete the message~~
     - ~~Have the bot say who posted the twitter link (prefereably without a ping)~~

Current bugs:
 1) for multi pictured tweets, the bot will sometimes not post the subsequent photos. But if you post the same tweet again, it will do as intended and send the vxtwitter link and the subsequent photots.
    - it might have to do with how I'm using the API or how discord works with their embeds. (If you have any idea please reach out to me via discord @ seeyang1#0010)
    - Turns out that the main vx branch has a fix of sorts for this so I've implemented that
