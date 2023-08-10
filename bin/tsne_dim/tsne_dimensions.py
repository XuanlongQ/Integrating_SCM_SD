import pandas as pd
from sklearn.manifold import TSNE

# Load CSV file
df = pd.read_csv('Integrating_SCM_SD/bin/output/tsne/original_tsne.csv')

# Separate string variables and their corresponding 300-dimensional vectors
strings = df.iloc[:, 0].values
vectors = df.iloc[:, 1:].values

# Perform t-SNE with 2 output dimensions
tsne = TSNE(n_components=2)
vectors_tsne = tsne.fit_transform(vectors)

# Visualize t-SNE results
import matplotlib.pyplot as plt

plt.scatter(vectors_tsne[:, 0], vectors_tsne[:, 1])
for i, txt in enumerate(strings):
    plt.annotate(txt, (vectors_tsne[i, 0], vectors_tsne[i, 1]))
plt.show()
