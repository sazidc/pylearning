# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

import random

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")
