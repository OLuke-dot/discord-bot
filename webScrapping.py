from urllib.request import urlopen
from bs4 import BeautifulSoup
from discord.ext import commands
import random


def trending_links(lista):
    url = 'https://www.youtube.com/feed/trending'
    conn = urlopen(url)
    html = conn.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    for tag in links:
        link = tag.get('href')
        if link is not None:
            if link[0:6] == '/watch':
                lista.append(link)

def trending_links(lista):
    url = 'https://www.youtube.com'
    conn = urlopen(url)
    html = conn.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    for tag in links:
        link = tag.get('href')
        if link is not None:
            if link[0:6] == '/watch':
                lista.append(link)

class webScrapping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def trending(self, message):
        links = []
        trending_links(links)
        for x in range(0:3):
            await message.channel.send('https://www.youtube.com' + links[x])

    @commands.command()
    async def yt(self, message):
        links = []
        yt_links(links)
        await message.channel.send('https://www.youtube.com' + random(links))

def setup(client):
    client.add_cog(webScrapping(client))
