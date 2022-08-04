# 정규식
# Regex

import re

s = 'hi'
print(re.match(r'hi',s))
print(re.match(r'hey',s))
print(re.match(r'hi1*',s))
print(re.match(r'hi+',s))

d = 'color'
print(re.match(r'col?',d))

f = '이 영화는 A등급 입니다.'
print(re.match(r'이 영화는 [ABCD]',f))

g = '이 영화는 F등급 입니다.'
print(re.match(r'이 영화는 [ABCD.]',g))

h = '이 영화는 F등급 입니다.'
print(h.split('이 영화는 ')[1].split('등급')[0])
print(re.match(r'이 (..)는 ([ABCDF])등급 입니다.',h))
print(re.match(r'이 (..)는 ([.])등급 입니다.',h))