# 문자열 포매팅이 없다면?
# ~님 수강기간이 7일 남았습니다.

name = '나야'
duration = 7

message = name + '님 수강기간이 ' + str(duration) + '일 남았습니다.'
print(message)

# a문자열 포매팅 사용시
message_format = f'{name}님 수강기간이 {duration}일 남았습니다.'
print(message_format)


# format 메서드
a = 'Hello {0} {1} {2}'.format('apple', 'pine', 'pen')
print(a)

# 순서대로 지정됨
b = 'Hello {} {} {}'.format('apple', 'pine', 'pen')
print(b)



# f-string 사용
name1 = 'apple'
name2 = 'pine'
name3 = 'pen'

c = f'Hello {name1} {name2} {name3}'
print(c)