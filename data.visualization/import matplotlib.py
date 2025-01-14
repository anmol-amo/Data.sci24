import matplotlib.pyplot as plt

kurs = ["science",
     "maths",
     "english",
     "geografy"]
points = [25, 20, 30, 10,]

plt.figure(figsize=(10, 8))
plt.barh(kurs, points, color="pink")

plt.xlabel("points", fontsize=12)
plt.ylabel("kurs", fontsize=12)
plt.title("school report", fontsize=16)
plt.tight_layout()

plt.show()