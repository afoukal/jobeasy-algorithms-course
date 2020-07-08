#Last problem from slides (Sum of odd numbers)

def row_sum_odd_numbers(n):
    return n**3


print(row_sum_odd_numbers(10))

#When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.  The arithmetical mean is the sum of all elements divided by the number of elements.
list_1 = [1,2,3,4,5,6,7,8,9,10,0]


def list_below_arithmetic_mean(list):
    return [i for i in list if i < sum(list)/len(list)]


print(list_below_arithmetic_mean(list_1))

#When given a list of elements find the two lowest elements. They can be equal to each other or different.


def two_min_elements_intigers(list):
    first_min_number = min(list)
    list.remove(first_min_number)
    second_min_number = min(list)
    return { "first lowest element" : first_min_number,
             "second lowest element" : second_min_number}


print(two_min_elements_intigers(list_1))

