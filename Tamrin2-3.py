# Hamid HajiRahimi
# Tamrin: 2-3
# Array of Length "n" with Non-Repeating Random Numbers

#####################################################

import random
while True:
    L=int(input('Specify The Desired Length of The Array: '))
    k=int(input('Enter Range Number of  Non-Repeating Random Numbers: '))

    if k<L:
        print('The Range Number must be bigger than Length of The Array!' '\nPlease Enter Range Number Again:')
        
    else:
        n=random.sample(range(0,k),L)
        print(n)
        break
        
        
   