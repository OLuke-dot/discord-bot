# discord-bot
My project of a simple discord bot with some basic commands. 
Project requires additional discord.py module for proper working, and inserting your Token in main.py file. 
Informations about cogs as well as about retrieving your bot Token are written below
# Full list of supported commands
!ping <br>
!kick <br>
!ban <br>
!unban <br>
<b>Web Scrapping</b> - Requires additional module, BeautifulSoup!
!trending <br>
!yt <br>

# Installing discord.py
Python 3.5.3 or higher is required

To install the library without full voice support, you can just run the following command: <br>
<b>Linux/macOS</b> <br>
<i>python3 -m pip install -U discord.py</i><br>

<b>Windows</b><br>
<i>py -3 -m pip install -U discord.py </i><br>

# Getting your discord bot token
1. Go to the Discord Developer Portal - <u>https://discordapp.com/developers/applications/</u>

2. If you already have a bot created, click it in the list. If you don’t have any discord bots, 
click the <b>“New Application”</b> button.

3. Give Your Bot a Name

4. Go over the menu on the left side of the screen and click <b>"Bot"</b>
It’s the icon that looks like a little puzzle piece.

5. Click the blue <b>"Add Bot" </b> button

6. You’ll see a green message, “A wild bot has appeared!”, as well as a “Token” and a blue link 
you can click called <b>“Click to Reveal Token”</b>.

7. Get your token and insert in in a main.py file

# Cogs
Cogs are so-called extensions that can be 'loaded' or 'unloaded' to your bot without stopping the whole program
When you download all files, <b>create a folder called 'Cogs' and copy its path to main.py file</b>.
By using commands 'load', 'unload' and 'reload' you can manage and activate your cogs. By using command !help on a discord chat,
you are able to see all avaliable commands as well as loaded and active cogs.
