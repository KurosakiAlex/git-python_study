# 在__init__中没有from .test import create_time
#因此可以使用另一种方法

# import file

import file.text
print(file.text.creat_time())



# 或者这样
from file import text
print(text.creat_time())








