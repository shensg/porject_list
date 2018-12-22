
import re

# 'Python' 普通字符         '\d' 元字符
a = 'C0C++7Java8C#9Pyhton6Javascript'
r = re.findall('\d', a)    # 匹配一个数字字符。等价于[0-9]。grep 要加上-P，perl正则支持
print(r)

r = re.findall('\D', a)    # 匹配一个非数字字符。等价于[^0-9]。grep要加上-P，perl正则支持
print(r)







