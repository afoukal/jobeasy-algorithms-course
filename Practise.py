num1= 10
index = 5

result_1 = num1 ** index

def power(num, index):
    if index == 0:
        return 0
    elif index == 1:
        return num
    elif index > 1:
        result = power(num, index -1)* num
        return result
    else:
        print("error message")


print(result_1)
print(power(num1, index))