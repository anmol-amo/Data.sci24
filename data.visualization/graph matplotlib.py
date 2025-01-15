"""
import matplotlib.pyplot as plt

labels = 'IT', 'Marketing', 'Data Science', 'Finance'
values = [500, 156, 300, 510]
explode = (0.05, 0.05, 0.05, 0.05) 
color = ("pink", "blue", "yellow", "orange")
plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=False, colors=color)
plt.show()
# to show pie charts
"""
"""""
import matplotlib.pyplot as plt
import seaborn as sns

categories = ["A", "B", "C"]
values = [10, 20, 30]

sns.set_theme(style="darkgrid")
sns.set_palette("muted")

sns.barplot(x="category", y="values", data={"category": categories, "values": values})
plt.title("Anpassat stapeldiagram")
plt.show()
"""

