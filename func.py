# numbers = [1, 2, 3, 4, 5]
# max_num = max(numbers) 

# print(max_num)

import random

random_number = random.randint(0, 2)

# print(random_number)

#######

menus = ['김밥', '라면', '만두']

# print(menus[random_number])

menu = random.choice(menus)
# print(menu)

numbers = range(1, 46)          # range : N <= A < N
lucky_number = random.sample(numbers, 6)         # random.sample(뽑을 범위, 갯수)
# print(sorted(luckynumber))       # sorted() : 오름차순으로 정렬해줌

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

# pip install requests
import requests

res = requests.get(URL)

data = res.json()

# print(data)


drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)
lotto_numbers = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]
print(lucky_number)
print(lotto_numbers)

print(set(lucky_number) & set(lotto_numbers))  # set : 집합의 형태로 바꿔줌, & = 교집함 

print(data['drwNoDate'])