#Task 2: Sum of Integers from 1 to 50 Using a  for Loop
#expected output= the sum of numbers from 1 to 50 is : 1275
#Range function
#first method
num = range(1,51)
total = 0
for i in num :
    total = total + i
    print(f"The sum of numbers form 1 to 50 is {total}")

#second method
# Task 2: Sum of Integers from 1 to 50 Using a for Loop

total = 0

for i in range(1, 51):
    total += i

print("The sum of numbers from 1 to 50 is :", total)