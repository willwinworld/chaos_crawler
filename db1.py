import requests
from pyquery import PyQuery as pq

def open_url(url):
    r = requests.get(url)
    d = pq(r.text)
    new_list = []
    movie_nodes = d('#content .article .item')
    for node in movie_nodes:
        dollor = pq(node)
        image = dollor('.nbg img').attr('src')
        title = dollor('.pl2 a').text().split('/')[0].strip()
        score = dollor('.rating_nums').text()
        review = dollor('.star.clearfix .pl').text()
        url = dollor('.pl2 a').attr('href')
        new_list.append({'image':image, 'title':title, 'score':score, 'review':review, 'url':url})
    return new_list
 
 
a = open_url('http://movie.douban.com/chart')
for i in a:
   url = i['url']
   r = requests.get(url) #r就是一个对象  人类就是一个类，具体的人就是对象
   d = pq(r.text)   #pq是一个函数，d是变量也是函数
   title = d('#link-report span').text() #所以才可以往d里面传参数
   print title
  
    
        
        
   
  
   


