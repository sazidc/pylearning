numbers = []
for number in range(1,21):
    numbers.append(number)

print("The first three items in the list are:")
print(numbers[:3])
print("Three items from the middle of the list are")
print(numbers[8:11])
print("The last three items in the list are:")
print(numbers[-3:])

my_pizzas = ['cheese pizza', 'jalapeno pizza', 'four seasons pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('oregano pizza')
friend_pizzas.append('special pizza')
#print(my_pizzas)
#print(friend_pizzas)
print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
print("\n")

restaurant_foods = ('rice', 'vegetable', 'chicken', 'fish', 'salad')
for food in restaurant_foods:
    print(food)
print("\n")
restaurant_foods = ('bread', 'vegetable', 'chicken', 'fish', 'ice cream')
for food in restaurant_foods:
    print(food)
