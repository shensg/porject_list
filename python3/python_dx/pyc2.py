
class Start():
    name = 'hello'
    age = 0
    # 区分开 '类变量' '实际变量'
    # 类变量和类关联在一起的
    # 实际变量是面向对象的
    def __init__(self, name, age):    #构造函数  __int__是双下滑线 '_'
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age
        # print('student')       

    def do_homework(self):    #普通函数
        print('homework')

    # 行为 和 特征
# class Printer():
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))

start1 = Start('蓝色', 18)
print(start1.name)
start2 = Start('红色', 16)
print(start2.name,start2.age)
# start3 = Start('兰', 15)
print(Start.name)
# print(id(start1))
# print(id(start2))
# print(id(start3))

# start1.print_file()


