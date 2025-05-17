import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

df = pd.read_csv("population.csv")

uk_data = df[(df["Entity"] == "United Kingdom") & (df["Year"] >= 1800) & (df["Year"] <= 1850)]

uk_data = uk_data.sort_values("Year")

# plt.figure(figsize=(10, 6))
# plt.plot(uk_data["Year"], uk_data["population_historical"], marker='o', linestyle='-', color='royalblue')
# plt.title("Population of the United Kingdom (1800–1850)")
# plt.xlabel("Year")
# plt.ylabel("Population")
# plt.grid(True)
# plt.tight_layout()

# plt.savefig("uk_pop.png")
# plt.show()

P0 = uk_data[uk_data["Year"] == 1800]["population_historical"].values[0]
C = 10000000

def logistic_model(t, r, K):
    return ((P0 - C) * np.exp(r * t)) / (1 + ((P0 - C) * (np.exp(r * t) - 1) / K)) + C

t_data = uk_data["Year"].values - 1800
# print(t_data)
P_data = uk_data["population_historical"].values

print(P_data)

r_values = [0.02 * i for i in range(101)]
K_values = [P0 * (1 + i / 3) for i in range(101)]

loss = -100
pred_r = 0
pred_K = 0

for r in r_values:
    for K in K_values:
        pred = logistic_model(t_data, r, K)
        if r2_score(P_data, pred) >= loss:
            loss = r2_score(P_data, pred)
            pred_r = r
            pred_K = K

print(loss)
print(pred_r)
print(pred_K)
print(logistic_model(t_data, pred_r, pred_K))

r = 0.16
K = 17250000

P_pred = logistic_model(t_data, pred_r, pred_K)

plt.figure(figsize=(10, 6))
plt.scatter(t_data + 1800, P_data, label="True", color='blue')
plt.plot(t_data + 1800, P_pred, label="Predict", color='black')
plt.title("Population of the United Kingdom (1800–1850)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("uk_pop_pred2.png")
plt.show()
