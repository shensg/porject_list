# 概括字符集
#  \d 数字   \D 非数字
#  \w   可以匹配  "A-Z a-z _ 0-9"    \W   非单词字符（非普通字符）
#  \s   空白字符     \S  非空白字符

import re

a = 'python1111java&6_ 78%php'

r  = re.findall('[0-9]', a)
print(r)

r  = re.findall('\w', a)     # 匹配包括下划线的任何单词字符。类似但不等价于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集。
print(r)

r  = re.findall('\W', a)     # 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
print(r)

r  = re.findall('\s', a)     # 匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
print(r)

r  = re.findall('\S', a)     # 匹配任何可见字符。等价于[^ \f\n\r\t\v]。
print(r)







