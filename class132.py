import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gravity_stars")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius,mass)
plt.title("Radius & Mass of the Stars")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,gravity)
plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

plt.scatter(radius,mass)
plt.title("Radius & Mass on Scatter")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

