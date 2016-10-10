import urllib
import urllib2
import re

def getHtml(url):
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent':user_agent}
	request = urllib2.Request(url, headers = headers)
	page = urllib2.urlopen(request)
	html = page.read()
	#print html
	return html

def getJoke(html):
	reg = r'<div.*?class="content.*?>.*?<span>(.*?)</span>'
	jokeRe = re.compile(reg, re.S)
	jokeList = re.findall(jokeRe, html)
	f = open('joke.txt', 'w+')
	
	for joke in jokeList:
		x = re.sub('<br/>', '\n', joke)
		f.write(x + '\n\n')
	
	f.close()
	return jokeList

html = getHtml("http://m.qiushibaike.com")
print getJoke(html)
