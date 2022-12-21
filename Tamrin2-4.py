# Hamid HajiRahimi
# Tamrin: 2-4
# Add the numbers before exiting

#####################################################

sum=0  
n=0 
M=0   
while True:
    a=input('To Exit Write: Exit   \nEnter Numbers for Addition Operations:' )
    
    if a=="exit":
        print('Sum of Numbers: ',sum)
        break
    n=n+1
    M=int(a)  
    sum=sum+M

   