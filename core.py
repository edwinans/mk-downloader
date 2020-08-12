#!/usr/bin/env python3
# -*- coding: utf8 -*-

import webbrowser
import requests
import time
from bs4 import BeautifulSoup
import time
import re


home_url = 'https://maktabkhooneh.org'
LOGIN_URL = 'https://maktabkhooneh.org/auth/login-authentication'

f = open("auth.txt")
username = f.read().strip()
password = f.read().strip()


HEADER = {
    'authority': 'maktabkhooneh.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en,fr;q=0.9,fa;q=0.8',
    'cookie': '_ga=GA1.2.1174870334.1593897931; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=32914fd2-cc14-1386-5e85-7fd56ea7e0de; pushNotification-shownCount-6940=5; _hjid=647d1cb5-9f37-42b7-b09d-d95672651b7b; MEDIAAD_USER_ID=603a0919-91bb-4c77-a8dc-cef7bcf1678a; _pk_id.2.cac7=092dbf46d52488fa.1595811701.1.1595811713.1595811701.; csrftoken=GkhpMPb6jyCaBRKrKbuWTX3faJcVLcPmcNhNJ9OqUZqyl5wYRUHJXibNvKQhHuDq; _pk_ref.2.c515=%5B%22%22%2C%22%22%2C1596495921%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.2.c515=*; _gid=GA1.2.556307092.1596495922; _5ef0bb165ab223644e64d243=true; analytics_session_token=bd123ca8-dad0-2b66-cd17-a0ad0d17c93e; yektanet_session_last_activity=8/4/2020; tlc=true; _pk_id.2.c515=092dbf46d52488fa.1593897931.15.1596496584.1596495921.',
}


HEADER_AUTH = {
    'authority': 'maktabkhooneh.org',
    'content-length': '0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://maktabkhooneh.org',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://maktabkhooneh.org/',
    'accept-language': 'en,fr;q=0.9,fa;q=0.8',
    'cookie': '_ga=GA1.2.1174870334.1593897931; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=32914fd2-cc14-1386-5e85-7fd56ea7e0de; pushNotification-shownCount-6940=5; _hjid=647d1cb5-9f37-42b7-b09d-d95672651b7b; MEDIAAD_USER_ID=603a0919-91bb-4c77-a8dc-cef7bcf1678a; _pk_id.2.cac7=092dbf46d52488fa.1595811701.1.1595811713.1595811701.; csrftoken=GkhpMPb6jyCaBRKrKbuWTX3faJcVLcPmcNhNJ9OqUZqyl5wYRUHJXibNvKQhHuDq; _gid=GA1.2.556307092.1596495922; analytics_session_token=bd123ca8-dad0-2b66-cd17-a0ad0d17c93e; yektanet_session_last_activity=8/4/2020; tlc=true; _pk_ref.2.c515=%5B%22%22%2C%22%22%2C1596500088%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.2.c515=092dbf46d52488fa.1593897931.16.1596500088.1596500088.; _pk_ses.2.c515=*; _5ef0bb165ab223644e64d243=true; __acsco=7cf0cbbbeb8d966db15821c2c91eb8fa',
    'x-requested-with': 'XMLHttpRequest',
}


GET_LINKS_HEADER = {
    'authority': 'maktabkhooneh.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%87%DA%A9-%D9%82%D8%A7%D9%86%D9%88%D9%86%D9%85%D9%86%D8%AF-CEH-mk641/',
    'accept-language': 'en,fr;q=0.9,fa;q=0.8',
    'cookie': '_ga=GA1.2.1174870334.1593897931; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=32914fd2-cc14-1386-5e85-7fd56ea7e0de; pushNotification-shownCount-6940=5; _hjid=647d1cb5-9f37-42b7-b09d-d95672651b7b; MEDIAAD_USER_ID=603a0919-91bb-4c77-a8dc-cef7bcf1678a; _pk_id.2.cac7=092dbf46d52488fa.1595811701.1.1595811713.1595811701.; _gid=GA1.2.556307092.1596495922; analytics_session_token=bd123ca8-dad0-2b66-cd17-a0ad0d17c93e; yektanet_session_last_activity=8/4/2020; tlc=true; _pk_ref.2.c515=%5B%22%22%2C%22%22%2C1596500088%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.2.c515=*; _5ef0bb165ab223644e64d243=true; __acsco=7cf0cbbbeb8d966db15821c2c91eb8fa; _pk_id.2.c515=092dbf46d52488fa.1593897931.16.1596501298.1596500088.;',
}


def get_links(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    chapter_units = soup.find_all('a', class_='chapter__unit', href=True)
    unit_links = []

    for unit in chapter_units:
        if(unit['title'] != 'کوییز'):
            unit_links.append(home_url + unit['href'])

    return unit_links

    

def get_dl_link(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    dl_link = soup.find_all('a', class_='button--round')
    for link in dl_link:
        link['href']




with requests.Session() as client:
    client.get(home_url, headers=HEADER)
    cookie_dict = client.cookies.get_dict()
    csrf = cookie_dict.get('csrftoken')
    print(f"csrf : {csrf}")
    LOGIN_DATA = {
        'csrfmiddlewaretoken': cookie_dict.get("csrftoken"),
        'tessera': username,
        'hidden_username': username,
        'password': password
    }
    res = client.post(LOGIN_URL, data=LOGIN_DATA, headers=HEADER_AUTH)
    print(f"login : {res.status_code}")
    cookie_dict = client.cookies.get_dict()
    print(cookie_dict.items())
    tmp = f"csrftoken={cookie_dict.get('csrftoken')}; sessionid={cookie_dict.get('sessionid')}"
    print(tmp)
    GET_LINKS_HEADER['cookie'] += tmp
    print(GET_LINKS_HEADER)
    page = client.get(
        f"{home_url}/course/آموزش-هک-قانونمند-CEH-mk641/", headers=GET_LINKS_HEADER)
    
    unit_links = get_links(page)
    print(unit_links)
    # dl_links = []
    # for link in unit_links:
    #     page = client.get(link, headers=GET_LINKS_HEADER)
    #     print(get_dl_link(page))
    #     dl_links.append(get_dl_link(page))
    
    # print(len(dl_links))

