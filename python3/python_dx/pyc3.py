
class Start():
    sum = 0
    name = 'hello'
    age = 0
    # 区分开 '类变量' '实际变量'
    # 类变量和类关联在一起的
    # 实际变量是面向对象的
    def __init__(self, name, age):    #构造函数  __int__是双下滑线 '_'
        # 构造函数
        # 初始化对象的属性
        name = name
        age = age
        # print('student')       
    
    # 行为 和 特征
    def do_homework(self):    #普通函数
        print('homework')

start1 = Start('蓝色', 18)
print(start1.__dict__)
# start3 = Start('兰', 15)
print(Start.__dict__)

class Printer():
    def print_file(self,name,age):
        print('name:' + self.name)
        print('age:' + str(self.age))





