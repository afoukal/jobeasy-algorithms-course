# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enters n manually. n > 0

from random import randint

n = int(input('Tell any number above 0? '))

number_1 = randint(10**(n-1), int(str(9)*n))
print(number_1)
result = 0

for digit in str(number_1):
    result += int(digit)

print(result)

#OR

sum = 0

while number_1 > 0:
    sum += int(number_1%10)
    number_1= int(number_1/10)

print(sum)

# 2.Find max number from 3 values, entered manually from a keyboard
a = int(input("Tell me number 1 "))
b = int(input("Tell me number 2 "))
c = int(input("Tell me number 3 "))
list_1 = [a, b, c]
print(max(list_1))
#OR
max = 0
if a>b and a>c:
    max = a
elif b>a and b>c:
    max = b
else:
    max = c
print(max)

# 3.Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

number_3 = 789456123
odd = 0
even = 0
for digit in str(number_3):
    if int(digit)%2 == 0:
        even +=1
    else :
        odd +=1
print(odd)
print(even)



