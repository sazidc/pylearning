current_users = ['Ruby', 'selena', 'miya', 'Layla', 'guini']
current_users_lower = [user.lower() for user in current_users]
new_users = ['ahri', 'miya', 'helena', 'layla', 'hilda']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.lower()} is not available")
    else:
        print("This username is available")