
import re
a = "'C0C++7Java8C#9Pyhton6Javascript'"
# re.findall('正则表达式', a)

r = re.findall('Pyhton', a)
if len(r) > 0 :
    print('字符串中包含Python')
print(r)

r = re.findall('PHP', a)
if len(r) > 0 :
    print('字符串中包含PHP')
else:
    print('字符串不包含PHP')



