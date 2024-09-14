from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
<head>
    ...
    <style>
    .jan {
        background-color: yellow;
    }
    ...
    .month {
        color: red;
    }
    </style>
</head>

<body>
...
<ul>
    <li class="month">一月</li>
    <ul class="jan">
        <li>一月一号</li>
        <li>一月二号</li>
        <li>一月三号</li>
    </ul>
    ...
</ul>
</body>
在 <head> 中, 你会发现有这样一些东西被放在 <style> 里面, 这些东西都是某些 class 的 CSS 代码. 比如 jan 就是一个 class. jan 这个类掌控了这个类型的背景颜色. 
所以在 <ul class="jan"> 这里, 这个 ul 的背景颜色就是黄色的. 而如果是 month 这个类, 它们的字体颜色就是红色.
'''

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/list.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')

# 找所有 class=month 的信息. 并打印出它们的 tag 内文字
month = soup.find_all('li', {"class":"month"})
print(month)
for m in month:
    print(m.get_text())




#或者找到 class =jan 的信息.然后在 < ul > 下面继续找 < ul > 内部的 < li > 信息.这样一层层嵌套的信息, 非常容易找到.
jan = soup.find_all('ul', {"class","jan"})
d_jan = jan.find_all('li')
for d in d_jan:
    # get_text()是BeautifulSoup库中的一个方法，用于提取标签中的文本内容。具体来说，get_text()
    # 会返回标签内部的所有文本，包括其子标签中的文本，但会去除HTML标签本身
    print(d.get_text())






