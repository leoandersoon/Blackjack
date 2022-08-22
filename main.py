import random

# Greeting
greet = "Welcome to blackjack! Good luck for you, be careful and stay clever!"
print(greet)

# CPU's playing
cpu_num1 = random.randint(0,10)
cpu_num2 = random.randint(0,10)

cpu_sum = cpu_num1 + cpu_num2

# User's playing
def take_input(user_num1, user_num2):
    user_num1 = int(input('Please enter a number which is between 0 and 10: '))
    user_num2 = int(input('Please enter a number which is between 0 and 10: '))
    user_sum = user_num1 + user_num2

    if user_num1 < 0:
        user_num1 = int(input('Please enter a number which is between 0 and 10: '))
    elif user_num1 > 10:
        user_num1 = int(input('Please enter a number which is between 0 and 10: '))
    else:
        pass
    
    print(f' 1st number of CPU: {cpu_num1} \n 2nd number of CPU: {cpu_num2} \n Sum of CPU numbers: {cpu_sum}')
# Comparing both
if cpu_sum > user_sum:
    print("You lost!")
else:
    print("You won!")
