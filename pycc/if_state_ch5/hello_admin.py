usernames = ['ryan', 'star', '','admin', '', 'dan', 'lama', 'prada']
usernames.clear()

'''
for username in usernames:
    if username == 'admin':
        print("Hello, Admin. would you like to see a status report?")
    elif username == '':
        print("We need to find some user")
    else:
        print(f"Hello, {username.title()}. good to see you back")
'''
if usernames:
    for username in usernames:
        if username == 'admin':
            print("HelAo admin, would you like to see a status report?")
        else:
            print(f"Hello {use.title()rname}, thank you for loggin in again!")
else:
    print("We need to find some users!")