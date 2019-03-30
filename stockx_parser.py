from stockxsdk import Stockx
import os
import urllib.request
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

stockx = Stockx()

email = '*************'
password = '************'
stockx.authenticate(email, password)

keyword=['Jordan','Yeezy','Off-White','Yeezy 350','Human Race','Ultra Boost','Zoom Fly']

# Keyword for searching sneakers on stockx.com

resp=stockx.search('Yeezy')
df=pd.DataFrame(resp)

for k in keyword:
    t=pd.DataFrame(stockx.search('k'))
    resp=pd.concat([resp,t])

#generate dataframe with url use to parsing

#here using already cleaned up csv file I have
df=pd.read_csv('output.csv')


#using 'thumbnail_url' creating folder

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
        
for index, row in df.iterrows():  
    s=row['thumbnail_url']
    a=[s.capitalize() for s in s.split('/')[3].split('Product')[0].split('-')]
    b='-'.join(a)[:-1]
    f='-'.join(a[0:3])
    createFilder('E:/StockX/'+f)


#parsing/scraping all images from website base on url
#chekcing if image is png or jpg type

img_cd=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']

for index, row in df.iterrows():  
    s=row['thumbnail_url']
    a=[s.capitalize() for s in s.split('/')[3].split('Product')[0].split('-')]
    b='-'.join(a)[:-1]
    f='-'.join(a[0:3])
    temp_url='https://stockx.com/'+df["url"][index]
    result = requests.get(temp_url)
    c=result.content
    soup = BeautifulSoup(c,"lxml")
    url=soup.find_all("img")[12].get('src')
    if('img01' in url):
        url=url.split('?')[0]
        x,y=url.split('img01')
        print (x,y)
        for i in img_cd:
            try:
                urllib.request.urlretrieve(x+'img'+i+y, 'E:/StockX/'+f+'/'+str(index)+'_'+i+'.jpg')
            except:
                error=True
                pass
    else:
        try:
            urllib.request.urlretrieve(url, 'E:/StockX/'+f+'/'+str(index)+'_'+i+'.png')
        except:
            pass
