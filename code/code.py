
# ----------------------------------------------------
# ---------- Bakery Orders Data ETL Process ----------
# ----------------------------------------------------


# Importing necessary libraries
import pandas as pd
import numpy as np
from scipy import stats # ---> For mode
import os


# ----- Step 1: Reading the dataset -----

# --Load csv file into a DataFrame
try:
    absolute_path = os.path.dirname(__file__)
    file_path = '../data/BakeryOrders.csv'
    full_path = os.path.join(absolute_path, file_path)

    df = pd.read_csv(full_path)
except FileNotFoundError:
    print(f"Error: File not found at {full_path}")
    exit()

# --Show all columns and 100 rows
pd.set_option('display.max_columns', None)       # Show all columns
pd.set_option('display.width', None)             # Disable line wrapping
pd.set_option('display.max_colwidth', None)      # Show full column content
pd.set_option('display.max_rows', 100)           # Show 100 rows

# --Display the data
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                          ------------------------------------------------------------                                                          ")
print("                                                                    ----- Dataset Before Manipulation -----                                                          ")
print("                                                          ------------------------------------------------------------                                                          ")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.head(100))


# ----- Step 2: Data Cleaning -----

# --Filling emails with 'noemail@example.com'
df.fillna({'Email': 'noemail@example.com'}, inplace = True)


# --Filling empty delivery status
df.fillna({'Delivery_Status': 'Pending'}, inplace = True)

# --Filling missing price values by taking mean item category wise

# Calculate mean price for each item
item_avg_price = df.groupby('Item_Name')['Price_per_item'].mean()

# Fill missing prices based on item mean
for i in range(len(df)):
    if pd.isna(df.loc[i, 'Price_per_item']):
        item = df.loc[i, 'Item_Name']
        df.loc[i, 'Price_per_item'] = int(item_avg_price[item])


# ----- Step 3: Data Transformation -----

# --Creating new column for storing the total price of the order
df['Total_Price'] = df['Quantity'] * df['Price_per_item']


# Display the data after manipulation
print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                          ------------------------------------------------------------                                                          ")
print("                                                                     ----- Dataset After Manipulation -----                                                          ")
print("                                                          ------------------------------------------------------------                                                          ")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(df.head(100))


# ----- Basic Mathematical Operations on Total Price -----

# Drop null values in Price to avoid errors in NumPy operations
price_array = df['Total_Price'].dropna().to_numpy()

# --Highest Price
highest_price = np.max(price_array)


# --Lowest Price
lowest_price = np.min(price_array)


# --Mean Price (Average)
mean_price = np.mean(price_array)


# --Median Price
median_price = np.median(price_array)


# --Mode Price
mode_price = stats.mode(price_array, keepdims = True).mode[0]


# --Standard Deviation
std_price = np.std(price_array)


# --Total Revenue
total_revenue = np.sum(price_array)


# --Count of all prices
count_prices = price_array.size

print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                          ------------------------------------------------------------                                                          ")
print("                                                            ----- Basic Mathematical Operations on Total Price -----                                                          ")
print("                                                          ------------------------------------------------------------                                                          ")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"{'Highest Price':25} : {highest_price:.2f}")
print(f"{'Lowest Price':25} : {lowest_price:.2f}")
print(f"{'Mean Price':25} : {mean_price:.2f}")
print(f"{'Median Price':25} : {median_price:.2f}")
print(f"{'Mode Price':25} : {mode_price:.2f}")
print(f"{'Standard Deviation':25} : {std_price:.2f}")
print(f"{'Total Revenue':25} : {total_revenue:.2f}")
print(f"{'Non-Null Price Count':25} : {count_prices}\n")

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")