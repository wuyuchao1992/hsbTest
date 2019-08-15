# coding:utf-8
from bs4 import BeautifulSoup
import requests

# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# # 请求首页后获取整个html界面
#
# blog = r.content# # 用html.parser解析html

# soup = BeautifulSoup(blog,"html.parser")
# # 获取所有的class属性为dayTitle,返回Tag类
# times = soup.find_all(class_="dayTitle")
#
# # for i in times: # 获取a标签的文本
# #     print(i.a.string)
#
# title = soup.find_all(class_="postTitle")
#
# # for i in title:
# #     print(i.a.string)
#
# desc = soup.find_all(class_="postCon")
#
# # for i in desc:
# #     # tag的.contents 属性可以将tag的子节点以列表的方式输出
# #     c = i.div.contents[0] # 第一个
# #     print(c)
#
# for i,j,k, in zip(times,title,desc):
#     print(i.a.string)
#     print(j.a.string)
#     print(k.div.contents[0])
#
# yoyo = open("yoyo.html",'r', encoding='UTF-8')
r = requests.get("https://www.qiushibaike.com/")
soup = BeautifulSoup(r.content,"html.parser") # soup对象
tag = soup.find_all(class_="content")
for i in tag:
    # tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出
    allTag = i.span.contents[0]
    print(allTag)
# tag1 = soup.head # <head tag
# print(soup.prettify())
# print(type(soup)) # 返回是tag对象
# print(tag1)
# tag2 = soup.title# title tag
# print(tag2)
# 如果有多个相同标签，返回的是第一个
# tag3 = soup.a    # <a tag
# print(tag3)
# print(soup.string)
# print(type(tag))
# string = tag.string # NavigableString对象
# print(type(string))
# comment = soup.b.string # comment 对象
# print(type(comment))

