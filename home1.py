import requests
from pyquery import PyQuery as pq

def loop_get(url):
    r = requests.get(url)
    d = pq(r.text)
    url_list = []
    link_nodes = d('#content .paginator a:lt(9)')
    #url_list.append('http://movie.douban.com/top250?start=0&filter=')
    for node in link_nodes: 
        url_list.append('http://movie.douban.com/top250' + pq(node).attr('href'))
    titles = []
    title_nodes = d('#content .article .grid_view a span.title') 
    for node in title_nodes:
            titles.append(node.text)
    return url_list, titles  #返回结构形式：（[2到10页的URL，以字符串的形式],[第一页的电影名，以字符串的形式](['','',''],['','',''])输入第二页的URL，可以得到第二页的电影名和除了第二页的URL，也就是第一页和3-10页的URL，以此类推
    
def read_film_names(each_url):
    r = requests.get(each_url)
    d = pq(r.text)
    titles = []
    title_nodes = d('#content .article .grid_view a span.title')
    for node in title_nodes:
        titles.append(node.text)
    return titles

def combine():                                           #loop_get返回的是两个参数那么就要用两个参数去接收，也就是这里的a和result去分别接收loop_get这个函数返回的两个值url_list和titles
    a,result = loop_get('http://movie.douban.com/top250')#接收形式是a = []  result = []   元祖的括号去掉了
                                                          #a的值是url_list，result的值是titles 
    for i in a:
        print i
        title = read_film_names(i)
        result.extend(title)
    return result

res = combine()
for i in res:
    print i.encode('gbk', 'ignore')


    
