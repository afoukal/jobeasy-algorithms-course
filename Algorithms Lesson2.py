# def fibonacci(n):
#     fibonacci_1 = 1
#     fibonacci_2 = 1
#
#     if n == 0:
#         print(0)
#     if n > 0:
#         print(fibonacci_1)
#     if n > 1:
#         print(fibonacci_2)
#     index = 0
#     while index < n - 2:
#         fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
#         index += 1
#         print(fibonacci_2)
#
#
# fibonacci(10)
import math



st = "fsdfsd234.4554s4234df+sf234442"
num = ".123456789*/-+"
result = ""
for item in st:
    if item in num:
        result += item
print(result)
if "*" in result:
    result2 = result.split("*")
    result3 =  int(result2[0]) * int(result2[1])
    print(round(result3))
elif "+" in result:
    result2 = result.split("+")
    result3 = int(result2[0]) + int(result2[1])
    print(round(result3))
elif "-" in result:
    result2 = result.split("-")
    result3 = int(result2[0]) - int(result2[1])
    print(round(result3))
elif "/" in result:
    result2 = result.split("/")
    result3 = int(result2[0]) / int(result2[1])
    print(round(result3))