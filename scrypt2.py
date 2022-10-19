import requests
import bs4
import re
import json

list_13 = []

class Client:


    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self, url):
        # url = 'https://som1.ru/shops/64071/'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('td')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)

        # del list_t[0:2]
        adress_l = list_t[2]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            block_name = str(block_name)
            block_name = re.split('<h1>', block_name)[1]
            block_name = re.split('</h1>', block_name)[0]



        # Any phones
        list_phones = []
        container_phone = soup.select('td')
        for phone_block in container_phone:
            self.parse_block(block=phone_block)
            phone_block = str(phone_block)
            list_phones.append(phone_block)
        phone_block = list_phones[5]
        phone_block = re.split('<td>', phone_block)[1]
        phone_block = re.split('</td>', phone_block)[0]
        phone_block = re.split(',', phone_block)

        list_anytime = []
        container_time = soup.select('td')
        for block_time in container_time:
            self.parse_block(block=block_time)
            block_time = str(block_time)
            list_anytime.append(block_time)
        time_block = list_anytime[8]
        time_block = re.split('<td>', time_block)[1]
        time_block = re.split('</td>', time_block)[0]

        # Latlon
        # lan_list=[]

        def fetch_coordinates(apikey, address):
            base_url = "https://geocode-maps.yandex.ru/1.x"
            response = requests.get(base_url, params={
                "geocode": address,
                "apikey": apikey,
                "format": "json",
            })
            response.raise_for_status()
            found_places = response.json()['response']['GeoObjectCollection']['featureMember']

            if not found_places:
                return None

            most_relevant = found_places[0]
            lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
            return lat, lon

        my_key = "505030f6-5b12-4162-8295-d7f7c48223ca"
        coords = fetch_coordinates(my_key, adress_l)
        norm_coords=[coords[0], coords[1]]


        # print(list_t)
        vocab = {
        "address": adress_l,
        "phones": phone_block,
        "latlon": norm_coords,
        "name": block_name,
        "working_hours": time_block
        }

        list_13.append(vocab)


    def parse_block(self, block):
        pass


    def run(self):
        text = self.load_page(url)
        self.parse_page(text=text)


if __name__ == '__main__':
    urls = [
        'https://som1.ru/shops/539467/',
        'https://som1.ru/shops/120882/',
        'https://som1.ru/shops/64071/',
        'https://som1.ru/shops/151877/',
        'https://som1.ru/shops/64072/',
        'https://som1.ru/shops/64068/',
        'https://som1.ru/shops/64067/',
        'https://som1.ru/shops/408658/',
        'https://som1.ru/shops/64069/',
        'https://som1.ru/shops/278351/',
        'https://som1.ru/shops/146332/',
        'https://som1.ru/shops/354764/',
        'https://som1.ru/shops/398172/',
        'https://som1.ru/shops/454325/',
        'https://som1.ru/shops/311526/',
        'https://som1.ru/shops/431729/',
        'https://som1.ru/shops/507705/',
        'https://som1.ru/shops/614211/',
        'https://som1.ru/shops/552624/',
        'https://som1.ru/shops/131067/',
        'https://som1.ru/shops/133702/',
        'https://som1.ru/shops/64106/',
        'https://som1.ru/shops/64070/',
        'https://som1.ru/shops/136241/',
        'https://som1.ru/shops/256331/',

    ]

    parser = Client()
    # parser.run()
    print(list_13)

    for url in urls:
        parser.load_page(url)
        parser.run()
    path = 'test_quest_2'
    with open(path, 'w') as f:
        json.dump(list_13, f, ensure_ascii=False)






