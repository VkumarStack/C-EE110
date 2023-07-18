import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF

df = pd.read_csv(r'C:\Users\Vivek\Documents\Visual Studio Code\C&EE110\Homework\ShearWallDriftCapacityData.csv')
df = df.to_numpy()

# Part A
plt.hist(df[:, 0], edgecolor="black")
plt.xlabel("Wall Slenderness")
plt.ylabel("Frequency")
plt.show()

plt.hist(df[:, 1], edgecolor="black")
plt.xlabel("Drift Capacity (%)")
plt.ylabel("Frequency")
plt.show()

# Part B
slenderness_ecdf = ECDF(df[:, 0])
drift_ecdf = ECDF(df[:, 1])

slenderness_range = np.linspace(min(df[:, 0]), max(df[:, 0]))
plt.plot(slenderness_range, slenderness_ecdf(slenderness_range))
plt.xlabel("Wall Slenderness")
plt.ylabel("Cumulative Frequency")
plt.title("Empirical Cumulative Distribution Function of Wall Slenderness")
plt.show()

drift_range = np.linspace(min(df[:, 1]), max(df[:, 1]))
plt.plot(drift_range, drift_ecdf(drift_range))
plt.xlabel("Drift Capacity (%)")
plt.ylabel("Cumulative Frequency")
plt.title("Empirical Cumulative Distribution Function of Drift Capacity")
plt.show()

# Part C
mean_slenderness = np.mean(df[:, 0])
mean_drift = np.mean(df[:, 1])
print(mean_slenderness)
print(mean_drift)

# Part D
st_dev_slenderness = np.sqrt(np.var(df[:, 0], ddof=1))
st_dev_drift = np.sqrt(np.var(df[:, 1], ddof = 1))
print(st_dev_slenderness)
print(st_dev_drift)

# Part E
plt.scatter(df[:, 1], df[:, 0])
plt.xlabel("Drift Capacity")
plt.ylabel("Wall Slenderness")
plt.title("Wall Slenderness versus Drift Capacity")
plt.show()

# Part F
print(np.cov(df[:, 0], df[:, 1], ddof=1)[0][1] / (st_dev_drift * st_dev_slenderness))