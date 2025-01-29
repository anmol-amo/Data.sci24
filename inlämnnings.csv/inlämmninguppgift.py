import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/Users/anmolwakas/Documents/data science/inlämnnings.csv/unemployed_refund.csv')
#print(df.head(10))
# Hantera saknade värden.
#print(df.isnull().sum())


# Calculating the average amount per person
#df['average_amount_per_person'] = df['amount_sek'] / df['persons']
#print(df.head(10))

#filtered_data = df[df['average_amount_per_person'] > 10000]
#print(filtered_data.head(10))


#grouped_data = filtered_data.groupby(['age range_year']).agg({
    #'persons': 'sum',          # Totalt antal personer
    #'days': 'sum',             # Totalt antal dagar
    #'amount_sek': 'sum',       # Totalt belopp i SEK
    
#})
#print(grouped_data.head())


# sparar fil som excel_fil
#file_path = ('/Users/anmolwakas/inlämmnings/inlänningpython.xlsx')
#df.to_excel(file_path, index=False)

#print(f"File saved successfully to {file_path}")


#den kommer att visa en arbetslöshetskurva enligt åldersgrupp.
df_2 = pd.read_excel('/Users/anmolwakas/inlämmnings/inlänningpython.xlsx')

# Display first few rows
print(df_2.head())

# Set figure size
plt.figure(figsize=(10, 11))

# Group data by "age range_year" and sum "average_amount_per_person"
df_grouped = df_2.groupby("age range_year")["average_amount_per_person"].sum().reset_index()

# Print unique values
print("Unique age ranges:")
print(df_grouped["age range_year"].unique())

# Create line plot
sns.lineplot(x="age range_year", y="average_amount_per_person", data=df_grouped, color="pink")

# Titles and labels
plt.title("Most Unemployed Age", fontsize=18)
plt.xlabel("Age Range (Years)", fontsize=14)
plt.ylabel("Total Average Amount per Person", fontsize=14)

# Show plot
plt.show()


'''''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#detta visar vilken åldersgrupp som har fått mest arbetslösa pengar.
amount_sek = ["10379026", "10379026", "24305196", "25236334", "19944259", "15865777", "12738537", "10620474", "12673773"]
age = ["-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60+"]

# Convert to DataFrame
df = pd.DataFrame({"amount_sek": amount_sek, "age": age})

# Convert amount_sek to numeric values
df["amount_sek"] = pd.to_numeric(df["amount_sek"])

# Set Seaborn theme
sns.set_theme(style="darkgrid")
sns.set_palette("muted")

# Create barplot
sns.barplot(x="amount_sek", y="age", data=df)

# Title
plt.title("Anpassat stapeldiagram")

# Show plot
plt.show()
'''

#den ska visa vilket år har dem betalat mest pengar.
#Gruppera datan och summera belopp
#grouped_data = df.groupby('year')['amount_sek'].sum()

# Hämta år och belopp
#x = grouped_data.index    # År
#y = grouped_data.values   # Summerade belopp

# # Kontrollera x och y har värden
#print("Labels (x)", x)
#print("Values (y)", y)

# # Skapa cirkeldiagram
#plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
#plt.title('Mest betalda år')
#plt.axis('equal')  # Gör cirkeln rund
#plt.show()
'''''
# så här var det året mellan 2020 och 2022 den mest arbetslösa perioden hittills.
file_path = ('/Users/anmolwakas/Documents/data science/inlämnnings.csv/unemployed_refund.csv')

# Read the CSV file
df = pd.read_csv(file_path)

plt.figure(figsize=(7, 9))
plt.scatter(df['year'], df['persons'], color='skyblue', alpha=0.9)

# Labels and title
plt.xlabel('year of Unemployed People')
plt.ylabel('persons')
plt.title('year of most unemloyment')

# Show the plot
plt.grid(False)
plt.show()
'''