# Hamid HajiRahimi
# Tamrin: 2-1
# Number Guessing Competition

#####################################################
n=1
import random
random_number=random.randint(0,50)

while True:
    User_Guess=int(input('Enter Your Guess Number: '))

    if User_Guess==random_number:
        print('You win after' , n , 'times')
        break
    elif User_Guess>random_number:
        print('Guess a Smaller Number:')
        n=n+1
    elif User_Guess<random_number:
        print('Guess a Bigger Number:')
        n=n+1
