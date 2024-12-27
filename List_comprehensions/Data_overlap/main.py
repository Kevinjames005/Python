with open("file1.txt") as f1:
    f1_list = [int(el) for el in f1]

with open("file2.txt") as f2:
    f2_list = [int(el) for el in f2]

result = [num for num in f1_list if num in f2_list]

print(result)