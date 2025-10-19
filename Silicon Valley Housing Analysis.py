import pandas as pd   # import pandas for working with table-like data

# Create a small database for Bay Area housing prices
data = {
    'city': ['San Jose', 'Sunnyvale', 'Mountain View', 'Palo Alto', 'Fremont'],
    'price': [1200000, 1350000, 1800000, 2200000, 950000]
}

#Converts the dictionary into a table.
df = pd.DataFrame(data)

#show the dataset
print("Housing Price Data：")
print(df)

# Basic analysis
average_price = df['price'].mean()
max_price = df['price'].max()
min_price = df['price'].min()

# Output
print("\nAverage price：", round(average_price, 2))
print("Highest price：", max_price)
print("Lowerest price：", min_price)

# Find out which cities have the highest and lowerest prices
max_city = df.loc[df['price'].idxmax(), 'city']
min_city = df.loc[df['price'].idxmin(), 'city']

print("\nCity with the highest price:：", max_city)
print("City with the lowerest price:：", min_city)