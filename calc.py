# 더하기 함수
def add(a, b):
    return a + b
# 빼기 함수
def sub(a, b):
    return a - b
# 곱하기 함수
def mul(a, b):
    return a * b
# 나누기 함수
def div(a, b):
    return a / b
# 입력받는 함수
def input_number():
    # Get input from the user
    num1 = int(input("첫번째 수 입력: "))
    operator = input("연산자 입력 (+, -, *, /): ")
    num2 = int(input("두번째 수 입력: "))
    return num1, operator, num2

# 시작
def say():
    print("계산기 프로그램!")

# Define the calculator function
def calculator(num1, operator, num2):

    # Calculate the result
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = sub(num1, num2)
    elif operator == "*":
        result = mul(num1, num2)
    elif operator == "/":
        result = div(num1, num2)
    else:
        print("Invalid operator!")
        return
    
    # Print the result
    print("결과는:", result)
    
# Call the calculator function
say() # 단순 출력
num1, operator, num2 = input_number()  # 연산 입력받기
calculator(num1, operator, num2)    # 실제 계산해서 결과 출력
