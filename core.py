#!/usr/bin/env python3
# -*- coding: utf8 -*-

import webbrowser
import requests
import time
from bs4 import BeautifulSoup
import time
import re
from headers import *

home_url = 'https://maktabkhooneh.org'
LOGIN_URL = 'https://maktabkhooneh.org/auth/login-authentication'

f = open("auth.txt")
username = f.read().strip()
password = f.read().strip()



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

