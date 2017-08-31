#http://www.yuntushuguan.com/firsttransfer.jsp?enc=79a2424ac5f85024ba3b8fe6fe736affbef1365ff2f2b30685130b9ec15e3d7dc4b5ea8d621cdc1d43b55f4b51ebac00a07db9cad3b5d6562b3f5fa3fd4ccfb32037a748e61fa0f6d14b2025248b6a2e2a88a340bafa42df62861888da48f9ec240218495f9c6e6c5463c846d15c22785654622c3a0f01b185b8e3fb30041f4c66d2dbac65340e306fb57fb339649d84&uniti

#coding=utf-8
# coding=gbk
import urllib
import re
import string
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
	#获取hostname
	hostname = "http://www.shengwukx.cn"
	#获取书名bookname
	regName = r'\<title\>(.+?)\<\/title\>'
	namere = re.compile(regName)
	namelist = re.findall(namere,html)
	bookname=namelist[0]
	import os
	#解决中文乱码的问题
	path = bookname.decode('utf-8').encode('gbk')
	#创建文件夹
	isExists=os.path.exists(path)
	if not isExists:
		os.makedirs(path)
	os.chdir(path)
	#获得jpgpath
	regPath = r'jpgPath:"(.+?)",'
	pathre = re.compile(regPath)
	pathlist = re.findall(pathre,html)
	jpgpath=pathlist[0]
	#获得起始页startpage
	regSp = r'ps:\'(.+?)-'
	spre = re.compile(regSp)
	splist = re.findall(spre,html)
	startpage=splist[0]
	#获得结束页endpage
	regEp = r'ps:\'\d*-(.+?)\','
	epre = re.compile(regEp)
	eplist = re.findall(epre,html)
	endpage=eplist[0]
	for i in range(string.atoi(startpage), string.atoi(endpage)+1):
		if i<10:
			pageUrl=hostname+jpgpath+"00000"+str(i)+"?zoom=2"
			pageName="00000"+str(i)
			print "正在下载第%s页".decode("utf-8").encode('gbk') % i
			urllib.urlretrieve(pageUrl,'%s.jpg' % pageName)
		elif i>9 and i<100:
			pageUrl=hostname+jpgpath+"0000"+str(i)+"?zoom=2"
			pageName="0000"+str(i)
			print "正在下载第%s页".decode("utf-8").encode('gbk') % i
			urllib.urlretrieve(pageUrl,'%s.jpg' % pageName)
		elif i>99 and i<1000:
			pageUrl=hostname+jpgpath+"000"+str(i)+"?zoom=2"
			pageName="000"+str(i)
			print "正在下载第%s页".decode("utf-8").encode('gbk') % i
			urllib.urlretrieve(pageUrl,'%s.jpg' % pageName)
		elif i>999 and i<10000:
			pageUrl=hostname+jpgpath+"00"+str(i)+"?zoom=2"
			pageName="00"+str(i)
			print "正在下载第%s页".decode("utf-8").encode('gbk') % i
			urllib.urlretrieve(pageUrl,'%s.jpg' % pageName)
		else:
			print "页码超出范围了！".decode("utf-8").encode('gbk')




	
rawurl = raw_input("请输入咨询到的地址: ".decode("utf-8").encode('gbk'))   

html=getHtml(rawurl)

#print html
getImg(html)

print "下载完成。".decode("utf-8").encode('gbk')