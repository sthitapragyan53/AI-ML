# in this example we are generate a random user profil picture using randomuser API
from randomuser import RandomUser

r = RandomUser()

users = r.generate_users(10)

for user in users:
    print("Name:", user.get_full_name())
    print("Picture:", user.get_picture())
    print("-" * 40)