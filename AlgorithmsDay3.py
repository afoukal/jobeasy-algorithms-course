# #reverse string
# str="Hello"
# print(str[::-1])
# print(''.join(reversed(str)))
# index=len(str)
# result = ''
# while index> 0:
#     result += str[index-1]
#     index -= 1
# print(result
#       )

#anagram check
# str_1= "heart"
# str_2 = "eart"
#
# str_1,str_2 = str_1.lower(),str_2.lower()
# if len(str_1) != len(str_2)  or str_1 == str_2:
#     print(False)
# for char in str_1:
#     if str_1.count(char) != str_2.count(char):
#         print(False)
# print(True)


#string compression
# string ="aaaabbbcc"
# counter = 1
# result = string[0]
# for index in range(len(string)-1):
#     if string[index] == string[index+1]:
#         counter += 1
#     else:
#         if counter > 1:
#             result += str(counter)
#         result += string[index+1]
#         counter = 1
# if counter > 1:
#     result += str(counter)
# print(result)


# #unique characters
# str_3 = "aaassaagggffthhjjeasghkjkxd"
# result = ''
# for char in str_3:
#     if char not in result:
#         result += char
# print(result)

#recursion



#power
number = 10
index = 3
result = 1
ind = 0
while ind < index:
    result *= number
    ind += 1
print(result)

