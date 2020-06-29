# Enter a string of words separated by spaces. Find the longest word. ###### I have found the first longest word, not the last one :)

str_1 = '  Hello     world I love                  Python Today is a good    weather    blablab'

def longest_word(string):
    longest_word = ''
    for item in string.split(' '):
        if len(item) > len(longest_word):
            longest_word = item
    return longest_word


print(longest_word(str_1))


# Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string, and words may be separated by several spaces). Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

def clear_string(string):
    return ' '.join(i for i in string.split(' ') if len(i) > 0)

print(clear_string(str_1))