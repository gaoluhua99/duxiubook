#coding=utf-8
# coding=gbk
import urllib.request
from urllib.parse import urlparse
import re
import string
from multiprocessing import  Pool
import sys,os,time



f = open("111111.jpg", 'wb')
pageUrl="http://www.shulikxhhx.cn/n/53dad567f8a453110e209167d98938dfMC180420443284/img0/DA420AFB75885538558CC47C65BEC0531A6711368164406FF6CBA4BADBA3C07FAEFC35804B2FC8AD8B1860EF12F2CA7DFA99C2B66893D3B1DB4F621F2815C6B1ADF5C9967D7A41D21F784E1DA411B2D4B1FEA75BD07821F5154AACCF9DF0CC6B7AF9F4A9C7A7A10D181D0A4BBE5F63118368/bf1/drs/14143168/2CE227A1430342A5877481E85B977D56/000100?zoom=2"
f.write((urllib.request.urlopen(pageUrl)).read())
f.close()