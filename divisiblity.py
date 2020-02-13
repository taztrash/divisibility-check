#python program checks whether the given number is divisible by both 2 and 5 using else if 
number = int(input("enter any positve integer : "))

if ((number % 2 == 0) and (number % 5 == 0)):
    print("given number {0} is divisible by 2 and 5".format(number))
else:
    print("given number {0} is not divisible by 2 and 5".format(number))    
