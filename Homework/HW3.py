import numpy as np
import matplotlib.pyplot as plt

# Question 1 Part A
damage = np.arange(1, 8)
damage_probability4 = np.array([0.1, 0.350, 0.220, 0.150, 0.1, 0.065, 0.015])

plt.stem(damage, damage_probability4)
plt.xlabel("Damage State")
plt.ylabel("Probability")
plt.title("Probability Mass Function, Category 4 Hurricane")
plt.show()

plt.step(damage, np.cumsum(damage_probability4), where='post')
plt.xlabel("Damage State")
plt.ylabel("Cumulative Probability")
plt.title("Cumulative Probability Mass Function, Category 4 Hurricane")
plt.show()

# Question 1 Part B
conditional_probabilities = np.array(([0.890, 0.050, 0.035, 0.015, 0.010, 0, 0], 
                                     [0.520, 0.320, 0.080, 0.050, 0.012, 0.010, 0.008], 
                                     [0.250, 0.450, 0.170, 0.075, 0.030, 0.020, 0.005], 
                                     [0.100, 0.350, 0.220, 0.150, 0.100, 0.065, 0.015],
                                     [0.030, 0.100, 0.250, 0.350, 0.160, 0.085, 0.025]))
hurricane_probabilities = np.array([0, 0.1, 0.3, 0.4, 0.2])
joint_probabilities = conditional_probabilities.T * hurricane_probabilities

marginal_damage_probability = np.sum(joint_probabilities, axis=1)
plt.stem(damage, marginal_damage_probability)
plt.xlabel("Damage State")
plt.ylabel("Probability")
plt.title("Marginal Probability Mass Function")
plt.show()

plt.step(damage, np.cumsum(marginal_damage_probability), where='post')
plt.xlabel("Damage State")
plt.ylabel("Probability")
plt.title("Cumulative Probability Mass Function")
plt.show()