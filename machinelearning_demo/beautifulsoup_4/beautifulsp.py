import requests
from bs4 import BeautifulSoup
import re

# 创建BeautifulSoup对象
# 当数据来源为本地文件时
# file = open("xxx.html")
# soup = BeautifulSoup(file, "lxml")

# 当数据来源为网络时
content = requests.get("https://mail.qq.com/").text
soup = BeautifulSoup(content, "lxml")

# 1 按标签名查找标签
print(soup.a)  # 获取第一个匹配到的a标签
print('1-------------------------------------------------1')
# 2 属性
print(soup.a.attrs)  # 获取标签中所有属性名与对应属性值的字典
print(soup.a.attrs["href"])  # 获取属性名对应的属性值
print(soup.a["href"])  # 获取属性名对应的属性值的简写
print(soup.a.string)  # 获取第一个匹配到的标签的内容
print(soup.a.text)  # 获取第一个匹配到的标签以及其所包含的子标签的所有内容
print('2-----------------------------------------------2')
# 3 函数
print(soup.a.get_text())  # 同soup.a.text
print(soup.find("a"))  # 同soup.a
print(soup.find("a", href="https://w.mail.qq.com/cgi-bin/loginpage?f=xhtml"))  # 根据属性值定位到第一个匹配到的标签,属性值也可用正则表达式 如：
print(soup.find("a",href=re.compile(r"^[h]")))

# 注意： 若属性名是 class 则需要在后面加个下划线,写成 class_
print('3----------------------------------------------3')
print(soup.find_all("a"))  # 获取匹配到的所有标签, 返回一个列表
print(soup.find_all(["a", "b"]))  # 可以获取多种类的标签
print(soup.find_all("a", limit=2))  # 获取前2个匹配到的标签
for demo in soup.find_all("a", limit=3):
    print(demo)  # demo等同于soup.a
    print(demo.attrs)
soup.select("选择器")
# 选择器包括：
# 	标签选择器：soup.select("a")
# 	ID选择器：soup.select("#xxx")
# 	类选择器：soup.select(".xxx")
# 	层级选择器：soup.select("div a") # 任意多级
# 	或是：soup.select("div > a") # 直系的一级
# 注意：select函数返回的永远是一个列表
