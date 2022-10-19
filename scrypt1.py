import requests
import bs4
import re
import json

list_12 = []

class Client:


    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self,url):
        # url = 'https://oriencoop.cl/sucursales/196'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('span')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)

        del list_t[0:3]
        # print(list_t)

        # Name
        list_name=[]
        container_name = soup.select('h3')
        for block_name in container_name:
            self.parse_block(block=block_name)
            block_name = str(block_name)
            block_name = re.split('<h3>', block_name)[1]
            block_name = re.split('</h3>', block_name)[0]
            list_name.append(block_name)
        list_name.pop(0)

        if len(list_name) > 1:
            phones_list = [list_t[3+i*5] for i in range(len(list_name))]
        else:
            phones_list = list_t[3:13]

        # Any phones
        new_list = []
        container_aphons = soup.select('a')
        for block_aphons in container_aphons:
            self.parse_block(block=block_aphons)
            aphons_block = block_aphons.get('href')
            new_list.append(aphons_block)
        anum_one = new_list[7]
        anum_one = re.split('tel:', anum_one)[1]
        anum_two = new_list[8]
        anum_two = re.split('tel:', anum_two)[1]


        # print(list_t)
        list_anytime = []
        if len(list_name) == 1:
            monana = list_t[5].replace('.', ':')
            monana = re.split(' ', monana)
            tarde = list_t[6].replace('.', ':')
            tarde = re.split(' ', tarde)

            mon_thu = f'mon-thu {monana[1]} - {monana[3]}  {tarde[1]} - {tarde[3]}'
            fri = f'fri {monana[1]} - {monana[3]}  {tarde[1]} - {tarde[10]}'
            list_anytime = [mon_thu, fri]
        else:

            monana_one = list_t[5].replace('.', ':')
            monana_one = re.split(' ', monana_one)
            tarde_one = list_t[6].replace('.', ':')
            tarde_one = re.split(' ', tarde_one)
            mon_thu = f'mon-thu {monana_one[1]} - {monana_one[3]} '
            fri = f'fri {tarde_one[1]} - {tarde_one[3]}'
            list_anytime.append([mon_thu, fri])

            monana_two = list_t[10].replace('.', ':')
            monana_two = re.split(' ', monana_two)
            tarde_two = list_t[11].replace('.', ':')
            tarde_two = re.split(' ', tarde_two)
            mon_thu = f'mon-thu {monana_two[1]} - {monana_two[3]} {tarde_two[1]} - {tarde_two[3]} '
            fri = f'fri {monana_two[1]} - {monana_two[3]} {tarde_two[1]} - {tarde_two[10]}'
            list_anytime.append([mon_thu, fri])

            monana_three = list_t[15].replace('.', ':')
            monana_three = re.split(' ', monana_three)
            tarde_three = list_t[16].replace('.', ':')
            tarde_three = re.split(' ', tarde_three)
            mon_thu = f'mon-thu {monana_three[1]} - {monana_three[3]} {monana_three[6]} - {monana_three[8]} '
            fri = f'fri {monana_three[1]} - {monana_three[3]} {tarde_three[2]} - {tarde_three[4]}'
            wknd=f'weekend {tarde_three[6]} - {tarde_three[8]}'
            list_anytime.append([mon_thu, fri, wknd])
            # print(list_anytime)


        # Latlon
        lat_list=[]
        container_url = soup.select('iframe')
        for block_url in container_url:
            self.parse_block(block=block_url)
            url_block = block_url.get('src')
            lat_list.append(url_block)
        lat_list.pop(0)

        lan_list=[]
        for lan in lat_list:
            new_lan = [float(re.split('!3d', lan)[1][0:10]), float(re.split('!2d', lan)[1][0:10])]
            lan_list.append(new_lan)

        # print(list_t)
        for i in range(len(list_name)):
            vocab = {
            "address": list_t[2+5*i],
            "phones": [anum_two, anum_one, phones_list[0]],
            "latlon": lan_list[i],
            "name": list_name[i],
            "working_hours": list_anytime[i]
            }

        list_12.append(vocab)


    def parse_block(self, block):
        pass


    def run(self):
        text = self.load_page(url)
        self.parse_page(text=text)


if __name__ == '__main__':
    urls = [
        'https://oriencoop.cl/sucursales/127',
        'https://oriencoop.cl/sucursales/165',
        'https://oriencoop.cl/sucursales/79',
        'https://oriencoop.cl/sucursales/167',
        'https://oriencoop.cl/sucursales/170',
        'https://oriencoop.cl/sucursales/173',
        'https://oriencoop.cl/sucursales/180',
        'https://oriencoop.cl/sucursales/182',
        'https://oriencoop.cl/sucursales/184',
        'https://oriencoop.cl/sucursales/187',
        'https://oriencoop.cl/sucursales/188',
        'https://oriencoop.cl/sucursales/194',
        'https://oriencoop.cl/sucursales/196',
        'https://oriencoop.cl/sucursales/208',
        'https://oriencoop.cl/sucursales/219',
        'https://oriencoop.cl/sucursales/231',
        'https://oriencoop.cl/sucursales/267',
        'https://oriencoop.cl/sucursales/312',

    ]

    parser = Client()
    # parser.run()
    for url in urls:
        parser.load_page(url)
        parser.run()
    path = 'test_quest_1'
    with open(path, 'w') as f:
        json.dump(list_12, f, ensure_ascii=False)






