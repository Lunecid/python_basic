# 1. 저장 : 변수, Variable

# 1. 숫자(int)
dust = 10
# 2. 글자(string)
dust = '5'
# 3. 참, 거짓(boolean)
dust = True # False

# print(dust)

dust_list = [10, 20, 0, 50, 100]    # 나열 시: list
# print(dust_list[3])

dust_dict = {                       # Key Value가 중요할 시: dict
    '서울': 100,
    '대전': 10,
    '부산': 50,
}
# print(dust_dict['부산'])

# 2. 조건

age = 10

if age > 20: 
    print('성인입니다')               # 들여쓰기를 이용하여 if문 내에 있다는 것을 확인
elif age > 8:
    print('청소년입니다')
else: 
    print('어린이입니다')

dust = 0

# dust 150보다 크다면 -> 매우나쁨
# 80~150 -> 나쁨
# 30~79 -> 보통
# 0~29 -> 좋음

if dust > 150:
    print('대기질이 매우 나쁩니다.')
elif dust > 79:
    print('대기질이 나쁩니다.')
elif dust > 29:
    print('대기질이 보통입니다.')
elif dust >=0:
    print('대기질이 좋습니다.')
else:
    print('대기질이 측정불가입니다.')

if 150 <= dust:
    print('대기질이 매우 나쁩니다.')
elif 80 <= dust < 150:
    print('대기질이 나쁩니다.')
elif 30 <= dust and dust < 80:
    print('대기질이 보통입니다.')
else:
    print('대기질이 좋습니다.')


# 3. 반복
menus = ['짜장면', '김밥', '라면', '피자']

n = 0
while n < 4:
    print(menus[n])
    n = n + 1

for menu in menus:          # for item in list : list의 내용을 조각, 조각낸 내용을 하나씩 꺼내서 새로운 변수로 할당, 그리고 그 새 변수를 출력
    print(menu)