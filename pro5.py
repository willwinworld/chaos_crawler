import requests
from pyquery import PyQuery as pq
r = requests.get('http://movie.douban.com/chart')
d = pq(r.text)
print d('#content .article .indent img').text()