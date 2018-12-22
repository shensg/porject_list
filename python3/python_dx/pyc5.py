class Start():
    sum = 0
    # name = 'hello'
    # age = 0
    # 实例方法: 定义传参数时 'self' 必须出现，调用时不需要出现 'self'
    def __init__(self, name, age):    #构造函数  __int__是双下滑线 '_'
        # 构造函数
        # self 关键字是初始化对象的属性
        self.name = name
        self.age = age
        self.__class__.sum += 1
        # print('当前人数为:' + str(self.__class__.sum)

    
    # 行为 和 特征
    # self代表的是实例，是对象
    # 实例方法
    def do_homework(self):    #普通函数
        print('homework')
    

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
    
    @staticmethod
    def add(x,y):
        print(Start.sum)
        # print(name)
        print('This is static method')


start1 = Start('蓝色',15)
start1.add(1,2)
Start.add(2,3)
# start1 = Start('红色', 18)
# start1.plus_sum()
# Start.plus_sum()
# start2 = Start('黑色', 16)
# Start.plus_sum()
# start3 = Start('蓝色', 15)
# Start.plus_sum()


