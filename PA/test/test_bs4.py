from bs4 import BeautifulSoup
import re
import urllib2

req = urllib2.urlopen('https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD')

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print 'Get all links'
links = soup.find_all('a')
print links
for link in links:
    print link.name, link['href'], link.get_text()

print 'Get img link'
link_node = soup.find('a', href='http://example.com/lacie')
print link_node.name, link_node['href'],link_node.get_text()

print 'Re match'
link_node = soup.find('a', href = re.compile(r'm/ti'))
print link_node.name, link_node['href'], link_node.get_text()

print 'Get words of line p'
p_node = soup.find('p', class_ = 'title')
print p_node.name, p_node.get_text()