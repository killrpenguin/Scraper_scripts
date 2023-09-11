from lxml import html
import requests

# Request the page
page = requests.get('https://feeds.megaphone.fm/darknetdiaries')

tree = html.fromstring(page.content)

links = tree.xpath('//enclosure[contains(@url,"mp3")]/@url')
names = []
for element in tree.xpath('//title[2]'):
    names.append(element.text)

new_names = [s.replace(':', ' -') for s in names]
final_name = [a.replace('"', '') for a in new_names]

for (track, link) in zip(final_name, links):
    with open(track + ".mp3", "wb") as f:
        tmp = requests.get(link)
        f.write(tmp.content)
        print(track + " Downloaded")
