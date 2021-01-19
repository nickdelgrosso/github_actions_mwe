import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(0, 1, size=(2000))
plt.hist(data, bins=41)
plt.savefig("results.pdf")