# import pandas as pd 

# # load the dfset 
# df = pd.read_csv("zomato.csv", encoding="ISO-8859-1")

# print(df.head())
# # delete duplicates 
# df = df.drop_duplicates(inplace=True)

# df.dropna(subset=["Cuisines"], inplace=True)
# # # df.dropna(subset=["Cuisines"], inplace=True)
# # # Display the first few rows of the dfset 

# # # filter columns 
# # df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# # # converting types 
# # df['has_table_booking'] = df['has_table_booking'].astype('bool')
# # df['has_online_delivery'] = df['has_online_delivery'].astype('bool')
# # df['is_delivering_now'] = df['is_delivering_now'].astype('bool')
# # df['votes'] = df.to_numeric(df['votes'], errors='coerce')

# # df = df[df['aggregate_rating'] <= 5.0]

# # df.reset_index(drop=True, inplace=True)

# # df.to_csv("zomato_cleaned.csv", index=False)


# new code snippet for data cleaning
import pandas as pd
import uuid


# Load with encoding fix
df = pd.read_csv("zomato.csv", encoding="ISO-8859-1")

df["Restaurant ID"] = df["Restaurant ID"].fillna(
    value=[uuid.uuid4().int >> 64 for _ in range(df["Restaurant ID"].isna().sum())]
)
# 1. Drop duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
df.dropna(subset=["Cuisines"], inplace=True)  # Drop rows missing key fields

# 3. Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 4. Convert types if needed
df['has_table_booking'] = df['has_table_booking'].map({'Yes': 1, 'No': 0})
df['has_online_delivery'] = df['has_online_delivery'].map({'Yes': 1, 'No': 0})
df['is_delivering_now'] = df['is_delivering_now'].map({'Yes': 1, 'No': 0})
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')
df['restaurant_id'] = df['restaurant_id'].values()

# 5. Remove outliers (optional)
df = df[df['aggregate_rating'] <= 5]

# 6. Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
