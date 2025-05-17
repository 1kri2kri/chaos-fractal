import matplotlib.pyplot as plt

data = []
with open('data100000.out', 'r') as file:
    for line in file:
        line = line.strip()
        data.append(float(line)) 

x = list(range(len(data)))

plt.figure(figsize=(15, 4))
plt.plot(x, data, marker='o')
plt.xlabel("100000 years")
plt.ylabel("Population")
plt.grid(True)
plt.tight_layout()

plt.savefig("game-100000.png")
plt.show()