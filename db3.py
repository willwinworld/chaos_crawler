import requests
from pyquery import PyQuery as pq

def loop_get(url):
    r = requests.get(url)
    d = pq(r.text)
    url_list = []
    link_nodes = d('#content .paginator a:lt(9)')
    for node in link_nodes: 
        url_list.append('http://movie.douban.com/top250' + pq(node).attr('href'))
    return url_list

def read_film_names(each_url):
    r = requests.get(each_url)
    d = pq(r.text)
    titles = []
    title_nodes = d('#content .article .grid_view a span.title')
    for node in title_nodes:
        titles.append(node.text)
    return titles

def combine():
    a = loop_get('http://movie.douban.com/top250')
    result = []
    for i in a:
        print i
        title = read_film_names(i)
        result.extend(title)
    return result

res = combine()
for i in res:
    print i.encode('gbk', 'ignore')
