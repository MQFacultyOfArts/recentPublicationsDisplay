#!/usr/bin/env python3

import feedparser
import pprint
import datetime
import dateparser
import os
import shutil
import re
from io import StringIO
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

shutil.rmtree('_posts', ignore_errors=True)
os.mkdir('_posts')

nouns = ["projects","prizes","publications"]
#nouns = ["clippings"]
for noun in nouns:
    rss_base_url = "https://researchers.mq.edu.au/en/organisations/faculty-of-arts/{}/?ordering=publicationYearThenTitle&descending=true&format=rss&page={}"

    feedintime=[True]
    for page in range(0,10):
        if True not in feedintime:
            break
        feedintime=[]
        feed = feedparser.parse( rss_base_url.format(noun,page) )
        items = feed["items"]
        for item in items:
            pprint.pprint(item)
            time = dateparser.parse(item[ "published" ], settings={'TIMEZONE': '+0000'})
            print(page, noun, time, feedintime.count(False))
            if time > datetime.datetime.now(tz=datetime.timezone.utc):
                continue
            elif time < datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(days=90):
                feedintime.append(False)
                continue
            else:
                feedintime.append(True)
            link = item[ "link" ]
            title = item[ "title" ]
            title_filename = re.sub(r"([^0-9a-zA-Z-]+)","-",strip_tags(title))

            file_name = "{}-{:02}-{:02}-{}-{}.md".format(time.year,time.month,time.day,noun,title_filename)
            file_name = re.sub(r"-+","-",file_name)

            file_name = file_name.replace('/', '')
            with open("_posts/{}".format(file_name),'w') as f:
                #value = item["content"][0]['value'].encode('utf-8')
                f.write('''---
layout: iframe
title: >
  {}
status: publish
published: true
date: {}-{}-{} 00:00:00
meta:
  _edit_last: "1"
type: post
tags:
iframe_src: "{}"
---
        '''.format(title, time.year,time.month,time.day, link))
            #f.write(value)

    

