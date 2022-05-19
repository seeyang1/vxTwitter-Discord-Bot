# vxTwitter-Discord-Bot
A side project utilizing discord.py API and the TwitFix repository


 to do list: 
1) ~~Make the bot be able to read if the twitter link has the twitter link at all (use regex for this)~~
2) ~~Have the bot delete the message~~
     - ~~Have the bot say who posted the twitter link (prefereably without a ping)~~
3) make the bot check to see if there's an embed or video at all within the tweet (there's no need to fix embeds if there's no image/video) 
   - might make it check only for videos as the main use for vxtwitter is for videos
   - have to figure out how to find if embed.image.url or embed.video.url is empty and if it is, don't apply the fix
