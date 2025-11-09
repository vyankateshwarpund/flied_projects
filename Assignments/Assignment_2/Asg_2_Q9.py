# A program to display the sum of all even numbers between 1 and 50 using a loop
#for loop
sum_even = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i

print("Sum of all even numbers between 1 and 50 is:", sum_even)

#while loop
i=1
sum_even=0
while i <= 50:
    if i % 2 ==0:
        sum_even+=i
    i+=1
print("Sum of all even numbers between 1 and 50 is:",sum_even)    

