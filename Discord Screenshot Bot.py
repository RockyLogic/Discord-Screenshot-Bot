from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import discord
import os
import datetime
import re
from discord.ext import commands

token = "Token" #Replace token here!
path = "C://Users/rocky/Desktop/Python/chromedriver.exe" #Replace Path Here

client = commands.Bot(command_prefix="!")
client = discord.Client()

print(f"[{datetime.datetime.now()}] Booting Up Discord Bot")

@client.event
async def on_ready():
    print(f"[{datetime.datetime.now()}] Successfully Booted Up Discord Bot")

@client.event
async def on_message(message):
    if "!screenshot" in message.content:
        print(f"[{datetime.datetime.now()}] [Server: {message.guild.name}][#{message.channel}][{message.author}]:'{message.content}'")
        
        #Setting up Chromium Settings
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless") 
        
        #Regex
        urls = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
        if len(urls.group()) == 0:
            await message.channel.send(f"<@{message.author.id}> make sure to paste the entire link (Include https:// or http://)")
        print (urls.group())
        

        #Selenium ScreenShot
        driver=webdriver.Chrome(options=chrome_options,executable_path=path)
        driver.get(urls.group())
        driver.set_window_size(1920, 1080)    
        driver.get_screenshot_as_file('screenshot.png')
        await message.channel.send(file=discord.File('screenshot.png'))
        await message.channel.send(f"<@{message.author.id}> Heres Your ScreenShot Of: {urls.group()}")
        os.remove('screenshot.png')
        driver.quit()

client.run(token)