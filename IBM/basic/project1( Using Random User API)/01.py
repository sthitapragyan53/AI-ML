# here we importing user name and email from randuser API

from randomuser import RandomUser

r = RandomUser()

users = r.generate_users(10)

for user in users:
    print("Name:", user.get_full_name())
    print("Email:", user.get_email())
    print("-" * 30)