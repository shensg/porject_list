
# 公开的 public   
# 没有双下划线开头的函数默认是公开的  def marking():
# 私有的 private
# 有双下划线的函数默认是私有的     def __marking():
# python的内置变量是前后都有双下划线  __int__

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
        self.__score = 0
        self.__class__.sum += 1
        self.__class__.sum += 1
        # print('当前人数为:' + str(self.__class__.sum)


    def marking(self,score):
        if score < 0:
            return '不能给负数的分数'       
        self.score = score
        # print(self.name + '本次得分为：' + str(self.score))

    
    # 行为 和 特征
    # self代表的是实例，是对象
    # 实例方法
    def do_homework(self):    #普通函数
        print('homework')
    
    def do_english_homework(self):
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
result = start1.marking(59)
start1.__score = -1
print(start1.__score)
# print(start1.__dict__)
# print(result)
# start1.marking = -1
# start1.do_homework()
# start1.do_english_homework()


