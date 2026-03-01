# How can the RandomUser API be integrated with Python to generate random user profiles and organize the retrieved data into a Pandas DataFrame and CSV file?

from randomuser import RandomUser
import pandas as pd

def get_users():
    r = RandomUser()
    users = []

    for user in r.generate_users(10):
        users.append({
            "Name": user.get_full_name(),
            "Gender": user.get_gender(),
            "City": user.get_city(),
            "State": user.get_state(),
            "Email": user.get_email(),
            "DOB": user.get_dob(),
            "Picture": user.get_picture()
        })

    return pd.DataFrame(users)

df_users = get_users()

# Print in terminal
print(df_users)

# Optional: save to CSV
df_users.to_csv("random_users.csv", index=False)