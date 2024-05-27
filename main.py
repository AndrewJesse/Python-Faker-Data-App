import pandas as pd
from faker import Faker

fake = Faker()

# Create a list to hold the fake user data
data = []

# Generate 10 fake users
for _ in range(10):
    user_data = {
        "Name": fake.name(),
        "Address": fake.address().replace('\n', ', '),
        "Text": fake.text(),
        "Email": fake.email(),
        "Phone Number": fake.phone_number(),
        "State": fake.state(),
        "Country": "United States"
    }
    data.append(user_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('fake_users.csv', index=False)

print("CSV file with fake users created successfully.")
