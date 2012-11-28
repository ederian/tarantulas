# -*- coding: utf-8 -*-
"""
author: bizlarkie
date: 11.28.12
"""

import urllib2, multiprocessing, re, csv, sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

balls = ['http://www.slideshare.net/slideshows_partial_1.xml',
 'http://www.slideshare.net/slideshows_partial_10.xml',
 'http://www.slideshare.net/slideshows_partial_11.xml',
 'http://www.slideshare.net/slideshows_partial_12.xml',
 'http://www.slideshare.net/slideshows_partial_13.xml',
 'http://www.slideshare.net/slideshows_partial_14.xml',
 'http://www.slideshare.net/slideshows_partial_15.xml',
 'http://www.slideshare.net/slideshows_partial_16.xml',
 'http://www.slideshare.net/slideshows_partial_17.xml',
 'http://www.slideshare.net/slideshows_partial_18.xml',
 'http://www.slideshare.net/slideshows_partial_19.xml',
 'http://www.slideshare.net/slideshows_partial_2.xml',
 'http://www.slideshare.net/slideshows_partial_20.xml',
 'http://www.slideshare.net/slideshows_partial_21.xml',
 'http://www.slideshare.net/slideshows_partial_22.xml',
 'http://www.slideshare.net/slideshows_partial_23.xml',
 'http://www.slideshare.net/slideshows_partial_24.xml',
 'http://www.slideshare.net/slideshows_partial_25.xml',
 'http://www.slideshare.net/slideshows_partial_26.xml',
 'http://www.slideshare.net/slideshows_partial_27.xml',
 'http://www.slideshare.net/slideshows_partial_28.xml',
 'http://www.slideshare.net/slideshows_partial_29.xml',
 'http://www.slideshare.net/slideshows_partial_3.xml',
 'http://www.slideshare.net/slideshows_partial_30.xml',
 'http://www.slideshare.net/slideshows_partial_31.xml',
 'http://www.slideshare.net/slideshows_partial_32.xml',
 'http://www.slideshare.net/slideshows_partial_33.xml',
 'http://www.slideshare.net/slideshows_partial_34.xml',
 'http://www.slideshare.net/slideshows_partial_35.xml',
 'http://www.slideshare.net/slideshows_partial_36.xml',
 'http://www.slideshare.net/slideshows_partial_37.xml',
 'http://www.slideshare.net/slideshows_partial_38.xml',
 'http://www.slideshare.net/slideshows_partial_39.xml',
 'http://www.slideshare.net/slideshows_partial_4.xml',
 'http://www.slideshare.net/slideshows_partial_40.xml',
 'http://www.slideshare.net/slideshows_partial_41.xml',
 'http://www.slideshare.net/slideshows_partial_42.xml',
 'http://www.slideshare.net/slideshows_partial_43.xml',
 'http://www.slideshare.net/slideshows_partial_44.xml',
 'http://www.slideshare.net/slideshows_partial_45.xml',
 'http://www.slideshare.net/slideshows_partial_46.xml',
 'http://www.slideshare.net/slideshows_partial_47.xml',
 'http://www.slideshare.net/slideshows_partial_48.xml',
 'http://www.slideshare.net/slideshows_partial_49.xml',
 'http://www.slideshare.net/slideshows_partial_5.xml',
 'http://www.slideshare.net/slideshows_partial_50.xml',
 'http://www.slideshare.net/slideshows_partial_51.xml',
 'http://www.slideshare.net/slideshows_partial_52.xml',
 'http://www.slideshare.net/slideshows_partial_53.xml',
 'http://www.slideshare.net/slideshows_partial_54.xml',
 'http://www.slideshare.net/slideshows_partial_55.xml',
 'http://www.slideshare.net/slideshows_partial_56.xml',
 'http://www.slideshare.net/slideshows_partial_57.xml',
 'http://www.slideshare.net/slideshows_partial_58.xml',
 'http://www.slideshare.net/slideshows_partial_59.xml',
 'http://www.slideshare.net/slideshows_partial_6.xml',
 'http://www.slideshare.net/slideshows_partial_60.xml',
 'http://www.slideshare.net/slideshows_partial_61.xml',
 'http://www.slideshare.net/slideshows_partial_62.xml',
 'http://www.slideshare.net/slideshows_partial_63.xml',
 'http://www.slideshare.net/slideshows_partial_64.xml',
 'http://www.slideshare.net/slideshows_partial_65.xml',
 'http://www.slideshare.net/slideshows_partial_66.xml',
 'http://www.slideshare.net/slideshows_partial_67.xml',
 'http://www.slideshare.net/slideshows_partial_68.xml',
 'http://www.slideshare.net/slideshows_partial_69.xml',
 'http://www.slideshare.net/slideshows_partial_7.xml',
 'http://www.slideshare.net/slideshows_partial_70.xml',
 'http://www.slideshare.net/slideshows_partial_71.xml',
 'http://www.slideshare.net/slideshows_partial_72.xml',
 'http://www.slideshare.net/slideshows_partial_73.xml',
 'http://www.slideshare.net/slideshows_partial_74.xml',
 'http:/p/www.slideshare.net/slideshows_partial_75.xml',
 'http://www.slideshare.net/slideshows_partial_76.xml',
 'http://www.slideshare.net/slideshows_partial_77.xml',
 'http://www.slideshare.net/slideshows_partial_78.xml',
 'http://www.slideshare.net/slideshows_partial_79.xml',
 'http://www.slideshare.net/slideshows_partial_8.xml',
 'http://www.slideshare.net/slideshows_partial_80.xml',
 'http://www.slideshare.net/slideshows_partial_81.xml',
 'http://www.slideshare.net/slideshows_partial_82.xml',
 'http://www.slideshare.net/slideshows_partial_83.xml',
 'http://www.slideshare.net/slideshows_partial_84.xml',
 'http://www.slideshare.net/slideshows_partial_85.xml',
 'http://www.slideshare.net/slideshows_partial_86.xml',
 'http://www.slideshare.net/slideshows_partial_87.xml',
 'http://www.slideshare.net/slideshows_partial_88.xml',
 'http://www.slideshare.net/slideshows_partial_89.xml',
 'http://www.slideshare.net/slideshows_partial_9.xml',
 'http://www.slideshare.net/slideshows_partial_90.xml',
 'http://www.slideshare.net/slideshows_partial_91.xml',
 'http://www.slideshare.net/slideshows_partial_92.xml',
 'http://www.slideshare.net/slideshows_partial_93.xml',
 'http://www.slideshare.net/slideshows_partial_94.xml']

def get_urls(url):
    # url is a url, duh!!
    #############################
    '''
    this function collects urls from the sites listed in 
    balls (the above list)
    '''
    #############################
    link = urllib2.urlopen(url).read()
    soup = BeautifulSoup(link,'xml')
    mid = soup.find_all('url')
    urls = []
    for mi in mid:
        if 'thumbnails' in mi.contents[0]:
            continue
        else:
            urls.append(str(mi.contents[0]).replace('<loc>','').replace('</loc>',''))
    return urls

def parse_shit(balls):
    # balls is a url
    #############################
    '''
    This function is doing the scraping.
    It collects the url of the page, the description, the title, and 
    categories. Not all pages have a description, so the output file may 
    be sparse.
    '''    
    #############################
    output = csv.writer(open('slideshare.txt','a+'),delimiter = '\t')
    print balls
    # Parse the page:
    link = urllib2.urlopen(balls).read()
    soup = BeautifulSoup(link)
    url = balls
    # Grab everything 
    description = soup.find('p', {'class':'descriptionExpanded notranslate'}).getText()
    title = soup.find('title').contents[0]
    categories = soup.findAll('a',{'href':re.compile('category')})
    cats = []
    for cat in categories:
        cats.append(cat.getText())
    if len(cats)>= 2:
        category = ', '.join(cats)
    else:
        category = cats[0]
    # Put it in a tuple
    item = (url,category,title,description)
    # Write it to the file
    output.writerow(item)

fields = ('url','category','title','description')
# Scrape in parallel. Set how many 'workers' to use
pool = multiprocessing.Pool(processes=16)
for yikes in balls:
    print yikes
    # First you get the urls
    urls = get_urls(yikes)
    # Then you get the information
    pool.map(parse_shit,urls)

   