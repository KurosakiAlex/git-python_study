'''下面说的很重要'''

'''
1. 选着要爬的网址 (url)
2. 使用 python 登录上这个网址 (urlopen等)
3. 读取网页信息 (read() 出来)
4. 将读取的信息放入 BeautifulSoup
5. 使用 BeautifulSoup 选取 tag 信息等 (代替正则表达式)
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup


# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')

# BeautifulSoup 将 HTML 内容解析成一个树形结构，使你能够方便地进行遍历和操作。
# 'html.parser' 指定了使用 Python 内置的 HTML 解析器          BeautifulSoup 还支持其他解析器，如 lxml 和 html5lib，你可以根据需要选择
soup = BeautifulSoup(html, 'html.parser')

#prettify() 方法会： 将 HTML 标签和内容按层次缩进;  为每个标签添加换行符，使得 HTML 结构更清晰
pretty_html = soup.prettify()

print(html)
print(pretty_html)
