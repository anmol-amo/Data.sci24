import matplotlib.pyplot as plt

labels = 'IT', 'Marketing', 'Data Science', 'Finance'
values = [500, 156, 300, 510]
explode = (0.05, 0.05, 0.05, 0.05) 

plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=False)
plt.show()