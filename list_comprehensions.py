#To make a new list of squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

#Filtering Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [ev_num for ev_num in numbers if ev_num % 2 == 0]
print(result)


