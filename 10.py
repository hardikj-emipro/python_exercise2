import functools

myList = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]
all_numbers = functools.reduce(lambda a, b: a + b, myList)
total_of_all_numbers = sum(all_numbers)
total_of_even_numbers = sum(map(lambda a: a if a % 2 == 0 else 0, all_numbers))
total_of_each_list = list(map(lambda a: sum(a), myList))
print('Total of each numbers of each list: ', total_of_all_numbers)
print('Total of even numbers of each list: ', total_of_even_numbers)
print('Total of sub list element: ', total_of_each_list)
