import requests
from pyquery import PyQuery as pq

r = requests.get('http://movie.douban.com/chart')
d = pq(r.text)
new_list = []
movie_nodes = d('#content .article .item')
for node in movie_nodes:
    dollor = pq(node)
    image = dollor('.nbg img').attr('src')
    title = dollor('.pl2 a').text()
    title = title.split('/')[0].strip()
    score = dollor('.rating_nums').text()
    review = dollor('.star.clearfix .pl').text()
    new_list.append({'image':image, 'title':title, 'score':score, 'review':review})
    
#for i in new_list:
    #print i

    
    
    
    
