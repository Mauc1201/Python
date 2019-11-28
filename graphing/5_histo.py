import numpy as np
import matplotlib.pyplot as plt

# Distribución normal
np.random.seed(19680801)

# media y desviación estándar
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g')

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

######## hicimos dos tipos de graficas, se muestran en los siguientes enlaces
1) http://localhost:8888/notebooks/Untitled3.ipynb?kernel_name=python3
2) http://localhost:8888/notebooks/Untitled4.ipynb?kernel_name=python3
