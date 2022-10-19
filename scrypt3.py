"""
Классы похожи друг на друга, уже по окончании создании скрипта задумался об наследовании :(
"""

import requests
import bs4
import re
import json

list_14 = []


class Client_one:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self, url):
        # url = 'https://www.ergonfoods.com/ergon-agora-east'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)
        del list_t[2:]
        adress_t = list_t[0]
        phone_s = list_t[1]
        phone_s = re.split('E', phone_s)[0][4:]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()

        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)
        time_work = list_time[1]
        # print(list_time)
        hours_work = re.split('Hours', time_work)[1]


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords=[coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_s],
            "latlon": norm_coords,
            "name": name_block,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page(url)
        self.parse_page(text=text)

class Client_two:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }


    def load_page(self, url):
        # url = 'https://www.ergonfoods.com/ergon-qatar'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)
        # del list_t[2:]
        adress_t = list_t[1]
        phone_s = list_t[2]
        phone_s = re.split('E', phone_s)[0][5:]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()
            # print(name_block)

        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)
        time_work = list_time[1]
        # print(list_time)
        hours_work = re.split('Hours', time_work)[1]
        # print(hours_work)


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords=[coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_s],
            "latlon": norm_coords,
            "name": name_block,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page(url)
        self.parse_page(text=text)

class Client_tree:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self, url):
        # url = 'https://www.ergonfoods.com/ergon-westfield-london'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)
        # del list_t[2:]
        adress_t = list_t[1]
        phone_s = list_t[2]
        phone_s = re.split('E', phone_s)[0][5:]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()
            # print(name_block)

        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)
        time_work = list_time[1]
        # print(list_time)
        hours_work = re.split('Hours', time_work)[1]
        hours_work = f'{hours_work}, {list_time[2]}, {list_time[3]}'
        # print(hours_work)


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords=[coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_s],
            "latlon": norm_coords,
            "name": name_block,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page(url)
        self.parse_page(text=text)

class Client_eae:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self):
        url ='https://www.ergonfoods.com/ergon-agora-east'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)
        del list_t[2:]
        adress_t = list_t[0]
        phone_s = list_t[1]
        phone_s = re.split('E', phone_s)[0][2:]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()

        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)

        time_work = list_time[2]
        hours_work = re.split('Hours', time_work)[1]


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords=[coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_s],
            "latlon": norm_coords,
            "name": name_block,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

class Client_ebh:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self):
        url ='https://www.ergonfoods.com/ergon-beach-house'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)
        # del list_t[3:]
        adress_t = list_t[2]
        phone_s = list_t[3]
        phone_s = re.split('E', phone_s)[0]
        phone_sone = re.split('M',phone_s)[0][3:]
        phone_stwo = re.split('M', phone_s)[1][1:]


        # Name
        container_name = soup.select('title')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()

        name_ock = re.split('—', name_block)[0]


        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)

        time_work = list_time[1]
        hours_work = re.split('Hours', time_work)[1]


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords = [coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_sone, phone_stwo],
            "latlon": norm_coords,
            "name": name_ock,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

class Client_balboa:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self):
        url ='https://www.ergonfoods.com/balboa-food'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)

        adress_t = list_t[1]
        phone_s = list_t[3]
        phone_s = re.split('E', phone_s)[0]
        phone_sone = re.split('M',phone_s)[0][3:]
        phone_stwo = re.split('M', phone_s)[1][1:]


        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()

        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)

        time_work = list_time[1]
        hours_work = re.split('Hours', time_work)[1]



        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords=[coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_sone, phone_stwo],
            "latlon": norm_coords,
            "name": name_block,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

class Client_elc:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self):
        url = 'https://www.ergonfoods.com/ergon-limassol-cyprus'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('h4')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            # print(block)
            list_t.append(block)
        # del list_t[2:]
        adress_t = list_t[1]
        phone_s = list_t[2]
        phone_s = re.split('E', phone_s)[0][5:]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()
            # print(name_block)

        # Working hours
        list_time = []
        container_time = soup.select('p')
        for block_time in container_time:
            self.parse_block(block=block_time)
            time_block = block_time.text.strip()
            list_time.append(time_block)
        time_work = list_time[1]
        hours_work = re.split('Hours', time_work)[1]
        hours_work = f'{hours_work}, {list_time[2]}'
        # print(hours_work)


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_t)
        norm_coords=[coords[0], coords[1]]

        # print(list_t)
        vocab = {
            "address": adress_t,
            "phones": [phone_s],
            "latlon": norm_coords,
            "name": name_block,
            "working_hours": hours_work
        }

        list_14.append(vocab)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

class Client_etg:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self):
        url = 'https://www.ergonfoods.com/ergon-to-go'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        global url_block
        soup = bs4.BeautifulSoup(text, 'lxml')
        container_span = soup.select('p')
        list_t = []
        for block_span in container_span:
            self.parse_block(block=block_span)
            block = block_span.text.strip()
            list_t.append(block)
        # del list_t[10:]
        adress_tone = list_t[0]
        adress_two = list_t[3]
        adress_three = list_t[7]
        phone_stwo = list_t[6][3:]

        # Name
        container_name = soup.select('h1')
        for block_name in container_name:
            self.parse_block(block=block_name)
            name_block = block_name.text.strip()

        # Working hours

        hours_workone = re.split('Hours', list_t[1])[1]
        hours_worktwo = re.split('Hours', list_t[4])[1]
        hours_worktree = re.split('Hours', list_t[8])[1]


        #
        # Latlon
        #
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
        coords = fetch_coordinates(my_key, adress_tone)
        norm_coordsone=[coords[0], coords[1]]
        coords = fetch_coordinates(my_key, adress_two)
        norm_coordstwo = [coords[0], coords[1]]
        coords = fetch_coordinates(my_key, adress_three)
        norm_coordstree = [coords[0], coords[1]]

        # print(list_t)
        vocab_one = {
            "address": adress_tone,
            "phones": [None],
            "latlon": norm_coordsone,
            "name": name_block,
            "working_hours": hours_workone
        }
        vocab_two = {
            "address": adress_two,
            "phones": [phone_stwo],
            "latlon": norm_coordstwo,
            "name": name_block,
            "working_hours": hours_worktwo
        }
        vocab_three = {
            "address": adress_three,
            "phones": [None],
            "latlon": norm_coordstree,
            "name": name_block,
            "working_hours": hours_worktree
        }

        list_14.append(vocab_one)
        list_14.append(vocab_two)
        list_14.append(vocab_three)
        # print(list_14)

    def parse_block(self, block):
        pass

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == '__main__':

    urls_tree = [
        'https://www.ergonfoods.com/ergon-westfield-london',
        'https://www.ergonfoods.com/ergon-kerkyra',
                ]

    urls_one = [
        'https://www.ergonfoods.com/ergon-nicosia-cyprus',
        'https://www.ergonfoods.com/ergon-skiathos',
        'https://www.ergonfoods.com/ergon-lefkada',
        'https://www.ergonfoods.com/ergon-santorini-volkan-on-the-rocks',

    ]

    urls_two = [
        'https://www.ergonfoods.com/ergon-qatar',
        'https://www.ergonfoods.com/ergon-deli-maddox-london',
        'https://www.ergonfoods.com/ergon-sani',
        'https://www.ergonfoods.com/ergon-deli-cuisine-aia-elvenizelos',
        'https://www.ergonfoods.com/ergon-house-athens',
        'https://www.ergonfoods.com/ergon-agora',

    ]



    parser = Client_one()
    # parser.run()
    for url in urls_one:
        parser.load_page(url)
        parser.run()

    parser_two = Client_two()
    # parser_two.run()
    for url in urls_two:
        parser_two.load_page(url)
        parser_two.run()

    parser_eae = Client_eae()
    parser_eae.run()

    parser_ebh = Client_ebh()
    parser_ebh.run()

    parser_balboa = Client_balboa()
    parser_balboa.run()

    parser_two = Client_tree()
    # parser_two.run()
    for url in urls_tree:
        parser_two.load_page(url)
        parser_two.run()


    parser_elc = Client_elc()
    parser_elc.run()

    parser_etg = Client_etg()
    parser_etg.run()

    print(list_14)


    path = 'test_quest_3'
    with open(path, 'w') as f:
        json.dump(list_14, f, ensure_ascii=False)
