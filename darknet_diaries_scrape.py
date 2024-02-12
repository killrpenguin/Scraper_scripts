from lxml import html
import os
import requests
from requests.exceptions import RequestException
import optparse


class Library:
    def __init__(self) -> None:
        """
        tree: integrate this into dn_page.
        
        local_files: Returns a hashmap of Podcasts already in my Music Folder.

        dn_names: A list of titles from the DN podcast website.

        dn_links: A list of direct links to the DN podcasts hosted on megaphone.
        
        """
        if self.dn_page is not None:
            self.tree = html.document_fromstring(self.dn_page.content)


    @property
    def local_files(self) -> dict:

        self.file_names = os.listdir(os.path.expanduser('~/Music/Darknet_Diaries_Podcasts'))

        self.loc_files_hmap = {k:v for k, v in zip(

            range(len(self.file_names)),
            
            self.file_names) if ' -' in v}

        return self.loc_files_hmap 


    @property
    def dn_page(self) -> requests.Response | None:
        try:
            return requests.get('https://feeds.megaphone.fm/darknetdiaries')

        except RequestException:
            
            return None

        
    @property
    def dn_names(self) -> list | None:
        if self.dn_page is not None:

            self.names = [element.text for element in self.tree.xpath('//title')
                          if 'Darknet Diaries' not in element.text]

            self.names = [a.replace(':', ' -').replace('"', '').strip('Ep ') for a in self.names]

            return self.names

    
    @property
    def dn_links(self) -> list | None:
        
        if self.dn_page is not None:
            
           self.links = self.tree.xpath('//enclosure[contains(@url,"mp3")]/@url')

           return self.links


    def sync_files(self) -> None:
        if self.dn_names is not None and self.dn_links is not None:

            if len(self.dn_names) == len(self.dn_links):

                for (track, link) in zip(self.dn_names, self.dn_links):

                    if track not in self.local_files.values():

                        with open(f'{track}.mp3', 'wb') as podcast:
                            a_file = requests.get(link)
                            
                            podcast.write(a_file.content)

                            print(f'{track} Downloaded')





def Main():                  

    library = Library()
    
    parser = optparse.OptionParser()

    parser.add_option(
        '-s',
        '--sync',
        help = 'Sync Darknet Diaries podcasts.')

    library.sync_files()


Main()

