import numpy as np
from sklearn.manifold import TSNE
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_components=2, perplexity=2).fit_transform(X)
print(X_embedded)
plt.figure()
plt.scatter(X_embedded[:,0],X_embedded[:,1])

plt.show()