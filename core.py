#!/usr/bin/env python3
# -*- coding: utf8 -*-

import webbrowser
import requests
from bs4 import BeautifulSoup


url = 'https://maktabkhooneh.org/course/آموزش-هک-قانونمند-CEH-mk641/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
chapter_units = soup.find_all('a', class_='chapter__unit', href=True, limit=None)
print(len(chapter_units))
# for unit in chapter_units:
    # webbrowser.open("https://maktabkhooneh.org"+unit['href'])
# print(html)
