
class Start():
    sum = 0
    name = 'hello'
    age = 0
    # 实例方法: 定义传参数时 'self' 必须出现，调用时不需要出现 'self'
    def __init__(self, name, age):    #构造函数  __int__是双下滑线 '_'
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age
        # print('student')
        print(age)
        print(name)      
    
    # 行为 和 特征
    # self代表的是实例，是对象
    # 实例方法
    def do_homework(self):    #普通函数
        print('homework')

start1 = Start('蓝色', 18)
print(start1.__dict__)
start1.do_homework
# start3 = Start('兰', 15)
# print(Start.__dict__)

