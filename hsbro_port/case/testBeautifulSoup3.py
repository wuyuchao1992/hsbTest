# coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.autohome.com.cn/4462/#pvareaid=100124")
# 用html.parser解析html
soup = BeautifulSoup(r.text,"html.parser")
# 获取所有的class属性为dayTitle,返回Tag类
carName = soup.find_all(class_="name")
for i in carName: # 获取a标签的文本
    print(i.string)