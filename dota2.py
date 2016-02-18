
import requests
from pyquery import PyQuery as pq

def open(url): 
    r = requests.get(url)
    d = pq(r.text)
    heros_url_list = []
    heros_node = d('.bg .r_bar_bg .hero_list .heroPickerIconLink')
    for hero_node in heros_node:
        heros_url_list.append(pq(hero_node).attr('href'))
    return heros_url_list 

sss = open('http://www.dota2.com.cn/heroes/')
print sss
