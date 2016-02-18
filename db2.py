import requests
from pyquery import PyQuery as pq

def open_url(url):
    r = requests.get(url)
    d = pq(r.text)
    new_list = []
    movie_nodes = d('#content .article .item')
    for node in movie_nodes:
        dollar = pq(node)   
        image = dollar('.nbg img').attr('src')
        title = dollar('.pl2 a').text().split('/')[0].strip()
        score = dollar('.rating_nums').text()
        review = dollar('.star.clearfix .pl').text()
        url = dollar('.pl2 a').attr('href')
        new_list.append({'image':image, 'title':title, 'score':score, 'review':review, 'url':url})
    return new_list

def final_results(url_inside):
    r = requests.get(url_inside)
    d = pq(r.text)
    summary = d('#link-report span').text()
    return summary

def run():
    a = open_url('http://movie.douban.com/chart')
    ret = []
    for i in a:
        print i['title']
        summary = final_results(i['url'])
        ret.append((i['title'], summary))
    return ret

res = run()
for i in res:
    print i[0], i[1][:40]
