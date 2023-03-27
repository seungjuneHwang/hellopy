# csv 파일에 있는 메뉴들 중에 하나를 추천해서 출력하는 프로그램
import random
import csv

# csv 파일에 있는 데이터를 읽어 온다
with open('menu.csv', newline='') as f:
    reader = csv.reader(f)
    menu_list = [row[0] for row in reader]
    #data = list(reader)

# 읽어온 데이터(메뉴)를 출력
print(menu_list)

# 읽어온 데이터중에 무작위로 하나를 꺼내옴
menu = random.choice(menu_list)
print('AI가 추천해주는 메뉴는? 두구두구두구두구')
# 가져온 데이터 하나를 출력
# print(menu) 
print(f'{menu} 입니다. 맛있게 드세요~')