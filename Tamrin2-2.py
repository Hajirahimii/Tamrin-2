# Hamid HajiRahimi
# Tamrin: 2-2
# Throw the Dice, If 6 comes up, throw again

#####################################################
import random

while True:

    Dice_Number=random.randint(1,6)


    if Dice_Number==6:
        print(Dice_Number)
        print('Luckyو Throw Again: ')
    else:
        print(Dice_Number)
        break
