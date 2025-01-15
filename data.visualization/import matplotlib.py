import matplotlib.pyplot as plt

kurs = ["science",
     "maths",
     "english",
     "geografy"]
points = [25, 20, 30, 10,]

plt.figure(figsize=(10, 8))
plt.bar(kurs, points, color="red")

plt.xlabel("points", fontsize=12)
plt.ylabel("kurs", fontsize=12)
plt.title("school report", fontsize=16)
plt.tight_layout()

plt.show()