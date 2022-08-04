s = 'apple'

print(s.find('e'))

arr = s.split('p')
print(arr)





a = '제 생일은 9월 입니다.'
# position
pos = a.find('생일은 ')
print(pos) # 2

print(a[6:7]) # 9
pos +=4
print(a[pos:pos+1])


bd = a.split('생일은 ')[1].split('월')[0]
print(bd)