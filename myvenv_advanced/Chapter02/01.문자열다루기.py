# 1.replace
# 문자열 교체

a = "오늘 날씨는 흐림 입니다."
print(a)
b = a.replace("흐림","맑음")
print(b)

# 2. find
# 문자열 찾기
c = 'Hello world'.find('world2')
print(c)

# 3. split
# 문자열 분리
d = '나이키신발 265 X1212 78000'.split()
print(d)

e = '나이키신발:265:X1212:78000'.split(':')
print(e)


# 4. 
# 문자열 공백 제거
f = '    Yeah      '.lstrip()
print(f)

f = '    Yeah      '.rstrip()
print(f)

f = '    Yeah      '.strip()
print(f)