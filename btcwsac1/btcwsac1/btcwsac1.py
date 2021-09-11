from lxml import html
import requests


page = requests.get('https://www.nytimes.com/crosswords/game/mini')
contents = html.fromstring(page.content)
ACROSS = contents.xpath('//*[@id="root"]/div/div/div[4]/div/main/div[2]/div[2]/article/section[2]/div[1]')