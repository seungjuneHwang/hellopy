import random

def mylotto():
    # 1 ~ 46 까지 번호 생성
    winning_numbers = random.sample(range(1, 46), 6)
    print('AI 로 뽑은 로또 추천 번호:', winning_numbers)


def lottery():
    print("Welcome to the lottery program!")
    
    # Ask the user to input their lottery numbers
    user_numbers = []
    for i in range(6):
        num = int(input("Enter number " + str(i+1) + ": "))
        user_numbers.append(num)
        
    # Generate the winning lottery numbers
    winning_numbers = random.sample(range(1, 50), 6)
    
    # Print the winning numbers
    print("The winning numbers are:")
    print(winning_numbers)
    
    # Check how many numbers the user guessed correctly
    num_correct = len(set(user_numbers) & set(winning_numbers))
    
    # Print the results
    if num_correct == 6:
        print("Congratulations! You won the jackpot!")
    elif num_correct >= 3:
        print("Congratulations! You guessed", num_correct, "numbers correctly.")
    else:
        print("Sorry, you did not win this time. Better luck next time!")
        
# Call the lottery function to run the program
# lottery()
mylotto()
