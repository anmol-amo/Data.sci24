


import pandas as pd
import matplotlib.pyplot as plt


file_path = '/Users/anmolwakas/Documents/data science/inlämnnings.csv/processed_data_befolkningsförändringar.csv'
data = pd.read_csv(file_path)

data['procentuellökning'] = data['folkmängd'].pct_change() * 100

data.sort_values(by='år', ascending=True, inplace=True)

print(data)



plt.figure(figsize=(12, 6))
bar_width = 0.35
index = range(len(data['år']))

plt.bar(index, data['födda'], bar_width, label='Födda', color='skyblue', edgecolor='black')
plt.bar([i + bar_width for i in index], data['döda'], bar_width, label='Döda', color='salmon', edgecolor='black')

plt.title('Relation mellan födda och döda per år')
plt.xlabel('År')
plt.ylabel('Antal personer')
plt.xticks([i + bar_width / 2 for i in index], data['år'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
