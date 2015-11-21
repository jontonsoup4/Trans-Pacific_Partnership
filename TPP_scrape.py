from bs4 import BeautifulSoup
import requests
import json
from collections import OrderedDict


class TPP:
    def __init__(self):
        self.url = 'https://medium.com/the-trans-pacific-partnership/table-of-contents-83d9de8d01b5'
        try:
            self.index = json.loads(open('TPP.json').read(), object_pairs_hook=OrderedDict)

        except FileNotFoundError:
            self.gather_data()

    def gather_data(self):
        self.load_index()
        for link in self.index.keys():
            self.index[link]['text'] = self.search(self.index[link]['url'])
            print(link)
        with open('TPP.json', 'w') as f:
            json.dump(self.index, f)

    def load_index(self):
        url = requests.get(self.url)
        soup = BeautifulSoup(url.text, 'html.parser')
        self.index = OrderedDict()
        index = self.index
        ch_num = 0
        for chapter in soup.find_all('h3')[:-5]:
            if chapter.find('a').text == 'Preamble':
                index['Preamble'] = {'title': chapter.find('a').text, 'url': chapter.find('a')['href']}
            else:
                index['Chapter {}'.format(ch_num)] = {'title': chapter.find('a').text, 'url': chapter.find('a')['href']}
            ch_num += 1

    def search(self, url):
        url = requests.get(url)
        soup = BeautifulSoup(url.text, 'html.parser')
        body = soup.find('div', {'class': 'section-content'})
        text = []
        for paragraph in body:
            for line in paragraph:
                if 'Read Previous Chapter' in line.text:
                    break
                if line.text == '':
                    continue
                text.append(line.text)
        return text

    def write_to_text(self):
        with open('TPP.txt', 'w') as f:
            for chapter in self.index:
                print(chapter)
                cur = self.index[chapter]
                f.write('*************** {} ***************'.format(chapter) + '\n\n')
                f.write('--- {} ---'.format(cur['title']) + '\n\n')
                f.write('url: ({})'.format(cur['url']) + '\n\n')
                for line in cur['text']:
                    f.write(line + '\n\n')
                f.write('\n')
            f.write('------------------------------' + '\n')
            f.write('''
######################################
### scrape by jontonsoup4          ###
### email: jontonsoup4@gmail.com   ###
######################################''')


TPP().write_to_text()
