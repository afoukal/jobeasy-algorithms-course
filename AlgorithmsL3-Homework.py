# Write a Python function, which will count how many times a character (substring) is included in a string. DON’T USE METHOD COUNT
char1 = 'ak'
string1 = 'aabbakkalab akblhaa'

def char_count(char,string):
    counter = 0
    for i in range(len(string)):
        if string[i:i+len(char)] == char:
            counter += 1
    return counter


# print(char_count(char1, string1))


# Find and replace a substring in a string for another substring. User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE
# string2 = 'hello world'
# old = 'world'
# new = 'Ana'
# result = []
# # for i in range(len(string2)):
# #     if string2[i:i+len(old)] != old:
# #         result.append(string2[i])
# #     else:
# #         string2[i:i + len(old)] = new
# #         result.append(string2[i:i+len(old)])
# # print(result)
# print(string2.replace(old, new))

# Write a function for decompressing string “a4b3c2d”
str_1 = 'a4b3cvf4'

def decompression_function(str):
    result = ''
    for i in range(len(str)-1):
        if str[i] in 'qwertyuiopasdfghjklzxcvbnm':
            if str[i+1] in '123456789':
                result += (str[i]*int(str[i+1]))
            else:
                result += str[i]
    if str[-1] in 'qwertyuiopasdfghjklzxcvbnm':
        result += str[-1]
    return result


# print(decompression_function(str_1))

# Recursion for Fib, factorial, digital root

# Fib
num_3 = 9
def fibonacci_seq(num):
    fib1 = 0
    fib2 = 1
    if num == 1:
        return fib1
    elif num == 2:
        return fib2
    else:
        return fibonacci_seq(num-1)+fibonacci_seq(num-2)

#print(fibonacci_seq(num_3))

# Factorial
number_1 = 4

def factorail(num):
    if num < 0:
        return "Are you sure you want to calculate Gamma functions"
    elif num == 1:
        return 1
    else:
        result = factorail(num-1) * num
    return result


#print(factorail(number_1))

# digital root
num2 = 12345678955

def digital_root(num):
    if len(str(num)) == 1:
        return num
    result = sum(int(i) for i in str(num))
    return digital_root(result)


#print(digital_root(num2))