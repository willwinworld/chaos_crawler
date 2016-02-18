import requests
from pyquery import PyQuery as pq

def loop_get(url):
    r = requests.get(url)
    d = pq(r.text)
    pre_results = []    
    link_nodes = d('#content .paginator a:lt(9)')
    pre_results.append('http://movie.douban.com/top250?start=0&filter=')
    for node in link_nodes: 
        pre_results.append('http://movie.douban.com/top250' + pq(node).attr('href'))
        pre_results.append({'url_list':url_list, 'title':title})
    return pre_results
    

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

#res = combine()
#for i in res:
#    print i.encode('gbk', 'ignore')

sss = loop_get('http://movie.douban.com/top250')
for i in sss:
    print i
    
