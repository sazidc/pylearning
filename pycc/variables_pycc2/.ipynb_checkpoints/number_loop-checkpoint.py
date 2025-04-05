#printing number with loop
for numbers in range(1,21):
    print(numbers)

#min, max, sum of a million numbers
number_list = list(range(1, 10**6+1))
print(min(number_list))
print(max(number_list))
print(sum(number_list))

#printing odd numbers
odd_numbers = []
for number in range(1,20,2):
    odd_numbers.append(number)
    print(number)

print(odd_numbers)

#list of 3
multiple_of_3 = list(range(3,30,3))
for number in multiple_of_3:
    print(number)

#cubic numbers
cubic_numbers = []
for value in range(1,11):
    value = value**3
    cubic_numbers.append(value)
    print(value)

print(cubic_numbers)

#cubic number by list comprehension
cubic_num = list(value**3 for value in range(1,11))
print(cubic_num)

