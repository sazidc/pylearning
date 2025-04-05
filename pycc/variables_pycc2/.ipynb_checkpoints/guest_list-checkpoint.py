#list of the special Guests
guest_list = ['abdul haq', 'sufia khatun', 'altaf hossain', 'jahanara begum']
print(len(guest_list))

#inviting the guests
message_1 = f"Honorable guest {guest_list[0].title()} you are invited to the ceremony"
message_2 = f"Honorable guest {guest_list[1].title()} you are invited to the ceremony"
message_3 = f"Honorable guest {guest_list[2].title()} you are invited to the ceremony"
message_4 = f"Honorable guest {guest_list[3].title()} you are invited to the ceremony"
print(message_1)
print(message_2)
print(message_3)
print(message_4)

#Replacing a guest who can't make it
print(f"It's very sad that {guest_list[0]} can not make it to the ceremony")
guest_list[0] = 'sadaruddin munshi'
print(len(guest_list))
message_1 = f"Honorable guest {guest_list[0].title()} you are invited to the ceremony"
print(message_1)
print(message_2)
print(message_3)
print(message_4)

#Adding more person cause found a bigger table
print("\nIt's my pleasure to announce that we have found a bigger table\n")
guest_list.insert(0, 'kazi nazrul islam')
guest_list.insert(3, 'tajuddin ahmad')
guest_list.append('mawlana bhasani')
print(len(guest_list))
message_1 = f"Honorable guest {guest_list[0].title()} you are invited to the bigger ceremony"
message_2 = f"Honorable guest {guest_list[1].title()} you are invited to the bigger ceremony"
message_3 = f"Honorable guest {guest_list[2].title()} you are invited to the bigger ceremony"
message_4 = f"Honorable guest {guest_list[3].title()} you are invited to the bigger ceremony"
message_5 = f"Honorable guest {guest_list[4].title()} you are invited to the bigger ceremony"
message_6 = f"Honorable guest {guest_list[5].title()} you are invited to the bigger ceremony"
message_7 = f"Honorable guest {guest_list[6].title()} you are invited to the bigger ceremony"
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
print(message_7)
print(guest_list)

#Ridiculously new table won't arrive anytime soon
print("\n\nWe are sorry to aanounce that we can only invite two people\n\n")
message_bad1 = f"We are extremely sorry we can not invite you to dinner {guest_list.pop(0).title()}"
message_bad2 = f"We are extremely sorry we can not invite you to dinner {guest_list.pop(0).title()}"
message_bad3 = f"We are extremely sorry we can not invite you to dinner {guest_list.pop(1).title()}"
message_bad4 = f"We are extremely sorry we can not invite you to dinner {guest_list.pop(1).title()}"
message_bad5 = f"We are extremely sorry we can not invite you to dinner {guest_list.pop(2).title()}"
print(len(guest_list))
print(message_bad1)
print(message_bad2)
print(message_bad3)
print(message_bad4)
print(message_bad5)
print(guest_list)

#inviting the remaining guests
print(f"Honorable Guest {guest_list[0].title()}, you are still invited")
print(f"Honorable Guest {guest_list[1].title()}, you are still invited")

#making an empty list
guest_list.remove('sufia khatun')
del guest_list[0]
print(guest_list)
print(len(guest_list))
