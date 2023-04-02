# Reverse of number and sum of digit

num=int(input("Enter the number"))

reversed_num = 0

sum = 0

while num != 0:

    digit = num % 10

    sum = sum + digit

    reversed_num = reversed_num * 10 + digit

    num = num//10

print("Reversed Number: ",reversed_num)

print('sum = ',sum)
