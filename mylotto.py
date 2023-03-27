import random

# 로또 번호를 만들어 주는 함수
def lotto():
    # 1 ~ 46 까지 번호 생성
    winning_numbers = random.sample(range(1, 46), 6)
    # print('AI 로 뽑은 로또 추천 번호:', winning_numbers)
    print(winning_numbers)

# 로또 5천원치 주세요 로또 번호 5개가 출력(1~5까지)
# for i in range(1, 6):
#     print(i)
#     lotto()

# print('번')
# 로또 천원치 주세요. 2천원 3천원... 
# 이 프로그램 사용자가 숫자를 입력하면 해당되는 갯수만큼 로또 번호를 생성하는 
# 프로그램을 작성하시오.
# 입력받기
a = int(input('로또 얼마치 드릴까요? 몇개 필요한지 숫자만 입력하세요:  '))
print(f'당신은 {a}개가 필요하군요.')
# a 값만큼 반복해서 로또 번호를 출력
for i in range(a):
    lotto() # 로또 번호 출력해주는 함수
    
print('여기 번호 나왔어요~')
