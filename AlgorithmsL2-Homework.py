# HW: Rewrite code, which will return only needed element of Fib sequence
import datetime


n = 10
f1 = 1
f2 = 1
index = 0
if n == 0:
    print(0)
else :
    while index < n-2:
        f1,f2 = f2, f2+f1
        index += 1
    print(f2)

# Use datetime library to solve problem Seconds to Date
# Write a Python program to convert seconds to day, hour, minutes and seconds.
sec = 10121
print(datetime.timedelta(seconds= sec))

# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

num = 960000
while num % 10 == 0:
    num = num//10
print(num)

# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

numb = 493193

while len(str(numb)) != 1:
    sum = 0
    for item in str(numb):
        sum += int(item)
    numb = sum
print(sum)