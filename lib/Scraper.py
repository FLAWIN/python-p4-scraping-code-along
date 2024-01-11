from bs4 import BeautifulSoup 
import requests
import ipdb
import Course
import json


class Scraper:
    def __init__(self):
        self.courses = []
    def get_page():
        # more code coming soon!
        doc =  BeautifulSoup(requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')
        ipdb.set_trace()

Scraper.get_page()
