#
#
# def recursion_fibonachi(n):
#     if n  <= 1:
#         return 1
#     else:
#         return recursion_fibonachi(n-1)+ recursion_fibonachi(n-2)
#
# print(recursion_fibonachi(6))

# from math import floor
#
# def split_in_half(str):
#     str_len = len(str)
#     half = floor(str_len/2)
#     if str_len % 2 != 0:
#         first = str[:half + 1]
#         second = str [half+ 1:]
#     else:
#         first= str[:half]
#         second = str[half:]
#     return f'{second}{first}'
#
#
# print(split_in_half('bbbbbaaaaa'))


def delete_fragment(string):
    first_index = 0
    last_index = 0
    index = 0
    while index < len(string):
        if string[index] == 'h':
            first_index = index
            break
        index += 1

    index = len(string)-1
    while index >=0:
        if string[index] == 'h':
            last_index = index
            break
        index -= 1

    return f'{string[:first_index]}{string[last_index+1]}'

print(delete_fragment('aaabbbhjjjjjjjjjjjjhkkl'))