# 字符集

import re

s = 'abc, acc, adc, afc, ahc'
r = re.findall('a[cf]c', s)     # 字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。
print(r)

r = re.findall('a[^cfd]c', s)   # 负值字符集合。匹配未包含的任意字符。例如，“[^abc]”可以匹配“plain”中的“plin”任一字符。
print(r)

r = re.findall('a[c-f]c', s)   # 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
print(r)


