# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:08:40 2017

@author: zxwan
"""
import re
import urllib2
import urllib
from bs4 import BeautifulSoup
import zipfile

#http://theme.npm.edu.tw/opendata/Authorize.aspx?sNo=04011013

url_pre="http://theme.npm.edu.tw/opendata/"

page_initial=18
page_end=18

open_url_pre="http://theme.npm.edu.tw/opendata/DigitImageSets.aspx?Key=^3^03000117&pageNo="

for i in range(page_initial,page_end+1):
    fetch_url=open_url_pre+str(i)
    response = urllib2.urlopen(fetch_url)  
    content = response.read() 
    
    soup = BeautifulSoup(content)
    #soup.final_all()
    raw_urls=soup.find_all(href=re.compile("Authorize\.as\S*[0-9]+"))
    
    print "Page:"+str(i)
    for raw_url in raw_urls:
        s_raw_url=str(raw_url)
        l_url=re.findall('Authorize\.as\S*[0-9]+',s_raw_url)
        url=l_url[0]
        target_url=url_pre+url;
        
     #   raw_name=re.findall('alt="\S+"',s_raw_url)
        raw_name=re.findall('[\x80-\xff]+',s_raw_url)
        folder_name=unicode(raw_name[0],"utf-8")
        name=unicode(raw_name[0]+'.zip',"utf-8")
        #download the file and unzip
        print("Downloading"+folder_name+":")
        urllib.urlretrieve(target_url, name)
        zip_ref = zipfile.ZipFile(name, 'r')
        try:
            zip_ref.extractall(unicode(raw_name[0],"utf-8"))
        except:
            print "解压缩失败！以原名（乱码）命名："
            zip_ref.extractall(raw_name[0])
        else:
            pass
        zip_ref.close()
        
    response.close()
    
    

    





