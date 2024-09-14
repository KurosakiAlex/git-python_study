'''
数据类型

查看数据类型；  type(变量名)

'''

#1. 整型数据 int->integer
num1 = 999
#print(f'num1 = {num1})  输出固定格式, f->format 格式化 ,特点就是在的那引号字符串中能够书写{}
print(f'num1 = {num1}，type(num1) = {type(num1)}') #格式化的输出，可读性高
# type(num1) = <class 'int'>   class表示类型,# num1是一个int整型数据

# 可读性不高，没有上面可读性高
print(num1)
print(type(num1))


#2. 浮点型(小数)  float
num2 = 66.6
print(f'num2 = {num2},type(num2) = {type(num2)}')


#3. bool 布尔型 -->只有两个结果，true/false
is_visited = True  # False
print(f'is_visited = {is_visited}，type(is_visited) = {type(is_visited)}')



#4. 字符串类型,有三种书写格式  1.单引号 2.双引号 3.三引号
# 复制快捷键ctrl + d
# 嵌套书写非常简单，不需要转义
name1 = '亚历克斯'
name2 = "亚历克斯"
name3 = '''亚历克斯'''
name4 = """亚历克斯"""


print(f'name1 = {name1},type(name1) = {type(name1)}')
# str -> string



# python中的高级数据类型(存储多个数据的类型)

#5.列表类型:特点，有序，可重复，可扩展
names = ['张三','李四','王五','张三','李四']
print(f'names = {names},type(names) = {type(names)}')



#6.元组类型:特点，有序，可重复，不可扩展
names = ('张三','李四','王五','张三','李四')
print(f'names = {names},type(names) = {type(names)}')
# 此时names的list数据已经被tuple覆盖了



#7.集合：特点，无序(通过算法实现，可能使用当前时间戳变量)，不可重复，可扩展
names = {'张三','李四','王五','张三','李四'}
print(f'names = {names},type(names) = {type(names)}')



#8. 字典类型：通过key去找值value  键值对/夫妻对  key -> value
stu_dict = {'stu_id' : '1001','name' : 'maria', 'age' : 18, 'score' : 100}
print(f'stu_dict = {stu_dict},type(stu_dict) = {type(stu_dict)}')
print(stu_dict['stu_id'])
print(stu_dict['score'])







