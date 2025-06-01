# make list with common numbers from both text files

with open('file1.txt') as f1:
    f1_data = [line.strip() for line in f1.readlines()]

with open('file2.txt') as f2:
    f2_data = [line.strip() for line in f2.readlines()]

result = [int(num) for num in f1_data if num in f2_data]
print(result)