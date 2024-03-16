#sum of the even number 

number = int(input("enter the number by user "))
sum_even = 0
for i in range(1, number+1):
    if i %2 == 0:
        sum_even += 1
    
print("the sum of the even numbers is ",sum_even)