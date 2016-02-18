import requests
from pyquery import PyQuery as pq

def loop_get(url):  #第一个函数的目的，给任意一个页面的URL，返回的是除去此页面的URL（即其它页面的URL）和输入页面的电影名
    r = requests.get(url) #获得URL链接
    d = pq(r.text) #读取此链接的内容，即HTML
    url_list = [] #赋值新的URL空列表，作为装URL的容器
    link_nodes = d('#content .paginator a:lt(9)') #用选择器获取其它页面不包括本页面的链接
    for node in link_nodes: #for循环的目的将9页的URL加入到url列表中
        url_list.append('http://movie.douban.com/top250' + pq(node).attr('href'))
    titles = [] #赋值新的titles的空列表作为装titles的容器
    title_nodes = d('#content .article .grid_view a span.title') #用选择器筛选出本页面的电影名
    #print '@@'*20
    #print type(title_nodes)
    for node in title_nodes: #for循环的目的将第一页的内容加入到titles的容器中
        titles.append(node.text)
    return url_list, titles #返回元祖，内容是排除第一页的URL，即2-10页的URL，还有第一页的title；如果输入第二页的URL，那返回的内容就是排除第二页的URL，和第二页的内容，以此类推

def combine():
    url1, result = loop_get('http://movie.douban.com/top250') #获得了2-10的URL列表，第一页的电影标题内容 注意是用列表的形式获得的
    for i in url1: #目的：遍历了2-10页URL，将2-10页的电影名加到titles的列表中
        print '@@'*20
        print i #打印了2-10页的URL的字符串
        urls, titles = loop_get(i) #获得了2-10的URL列表，第一页的电影标题内容列表
        result.extend(titles) #将2-10页的电影名加了进去，任务完成
        break
    return result

#res = combine()
#for i in res:
    #print i.encode('gbk', 'ignore') 
    #break
    
combine()


#检查函数“内部”的print结果，比如loop_get里，要看title_nodes的类型，那么直接如上图注释所做，同时调用loop_get('输入的URL链接')
#检查函数“外部”的return的结果，采用变量赋值的方法
#sss = loop_get('输入的URL链接')
#print sss