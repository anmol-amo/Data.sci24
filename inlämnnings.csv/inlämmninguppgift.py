import pandas as pd
import numpy as np
df = pd.read_csv('/Users/anmolwakas/Documents/data science/inlämnnings.1.csv/unemployed_refund.csv')
print(df.head(10))
# Hantera saknade värden.
print(df.isnull().sum())


# Calculating the average amount per person
df['average_amount_per_person'] = df['amount_sek'] / df['persons']
print(df.head(10))

filtered_data = df[df['average_amount_per_person'] > 10000]
print(filtered_data.head(10))


grouped_data = filtered_data.groupby(['age range_year']).agg({
    'persons': 'sum',          # Totalt antal personer
    'days': 'sum',             # Totalt antal dagar
    'amount_sek': 'sum',       # Totalt belopp i SEK
    
})
print(grouped_data.head())


# sparar fil som excel_fil
file_path = ('/Users/anmolwakas/Documents/data science/unemployed_refund.csv')
df.to_excel(file_path, index=False)

print(f"File saved successfully to {file_path}")

import matplotlib.pyplot as plt
import seaborn as sns
'''
''''''''
df_2= pd.read_excel('/Users/anmolwakas/inlämmnings/inlänningpython.xlsx')
print(df_2.head())

plt.figure(figsize=(10 , 9))

x = df_2["average_amount_per_person"]
y = []

y_unique = df_2["age range_year"].unique()
print("Y unique")
print(y_unique)

for y_val in y_unique:
    stringified = str(y_val)
    y.append(stringified)

print("String y")
print(y)

sns.lineplot(y_unique["average_amount_per_person"].sum(), y_unique["age range_year"], color="pink")
plt.title("most_unemployed_age", fontsize= 18)
plt.xlabel("age range_year", fontsize=14)
plt.ylabel("frequency", fontsize=14)
#plt.show()
'''

# amount_sek = ["10379026", "10379026", "24305196", '25236334', '19944259', '15865777']
# age = ["-24", "25-29", "30-34", "35-39", "40-44", "45-49"]

# sns.set_theme(style="darkgrid")
# sns.set_palette("muted")

# sns.barplot(x="amount_sek", y="age", data={"amount_sek": amount_sek, "age": age})
# plt.title("Anpassat stapeldiagram")
# # plt.show()

# import matplotlib.pyplot as plt

# # Gruppera datan och summera belopp
# grouped_data = df.groupby('year')['amount_sek'].sum()

# # Hämta år och belopp
# x = grouped_data.index    # År
# y = grouped_data.values   # Summerade belopp

# # Kontrollera x och y har värden
# print("Labels (x)", x)
# print("Values (y)", y)

# # Skapa cirkeldiagram
# plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
# plt.title('Mest betalda år')
# plt.axis('equal')  # Gör cirkeln rund
# plt.show()


plt.figure(figsize=(12, 6))
bar_width = 0.35
index = range(len(df['year']))

plt.bar(index, df['age range_year'], bar_width, label='age range_year', color='skyblue', edgecolor='black')
plt.bar([i + bar_width for i in index], df['persons'], bar_width, label='persons', color='salmon', edgecolor='black')

plt.title('Relation mellan födda och döda per år')
plt.xlabel('year')
plt.ylabel('Avg. age personer')
plt.xticks([i + bar_width / 2 for i in index], df['year'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()