'''很重要'''
'''
选着要爬的网址 (url)
使用 python 登录上这个网址 (urlopen等)
读取网页信息 (read() 出来)
将读取的信息放入 BeautifulSoup
使用 BeautifulSoup 选取 tag 信息等 (代替正则表达式)
'''

'''
网页信息:
<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>Scraping tutorial 1 | 莫烦Python</title>
    <link rel="icon" href="https://mofanpy.com/static/img/description/tab_icon.png">
</head>
<body>
    <h1>爬虫测试1</h1>
    <p>
        这是一个在 <a href="https://mofanpy.com/">莫烦Python</a>
        <a href="https://mofanpy.com/tutorials/scraping">爬虫教程</a> 中的简单测试.
    </p>

</body>
</html>
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)
'''
读取这个网页信息, 我们将要加载进 BeautifulSoup, 以 lxml 的这种形式加载. 除了 lxml, 其实还有很多形式的解析器,
不过大家都推荐使用 lxml 的形式. 然后 soup 里面就有着这个 HTML 的所有信息.
'''
soup = BeautifulSoup(html, features='lxml')

# 如果你要输出 <h1> 标题, 可以就直接 soup.h1.
print('\n', soup.h1)

print('\n', soup.p)

all_href = soup.find_all('a')
print(all_href)

'''
l：每次循环中，l 是 all_href 列表中的一个 BeautifulSoup 对象，代表一个 <a> 标签。
l['href']：使用 BeautifulSoup 对象 l 的属性访问方式获取 href 属性的值。
'''
all_href = [l['href'] for l in all_href]
print('\n', all_href)



