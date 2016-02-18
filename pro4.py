
import requests

def open_url(url):
    f = requests.get(url)
    return f.text
    
a = open_url('http://movie.douban.com/chart')
print a