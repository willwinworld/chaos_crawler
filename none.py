import requests
from pyquery import PyQuery as pq

def loop_get(url):  
    r = requests.get(url) 
    d = pq(r.text) 
    url_list = [] 
    link_nodes = d('#content .paginator a:lt(9)') 
    for node in link_nodes: 
        url_list.append('http://movie.douban.com/top250' + pq(node).attr('href'))
    titles = [] 
    title_nodes = d('#content .article .grid_view a span.title') 
    #print '@@'*20
    #print type(title_nodes)
    for node in title_nodes: 
        titles.append(node.text)
    return url_list, titles 

def combine():
    url1, result = loop_get('http://movie.douban.com/top250') 
    for i in url1: 
        print '@@'*20
        print i 
        urls, titles = loop_get(i) 
        result.extend(titles) 
        break
    return result

#res = combine()
#for i in res:
    #print i.encode('gbk', 'ignore') 
    #break
    
combine()

