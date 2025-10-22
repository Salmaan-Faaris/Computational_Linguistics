
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import numpy as np


sentences = [
    ["king", "queen", "man", "woman", "prince", "princess"],
    ["dog", "cat", "lion", "tiger", "elephant", "bear"],
    ["apple", "banana", "mango", "grape", "orange"],
    ["car", "bus", "truck", "train", "bicycle", "airplane"],
    ["math", "physics", "chemistry", "biology", "science"],
    ["happy", "sad", "angry", "joyful", "depressed"],
]

model = Word2Vec(sentences, vector_size=50, window=3, min_count=1, sg=1, epochs=100)


words = list(model.wv.key_to_index)
X = np.array([model.wv[word] for word in words])


num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)


tsne = TSNE(n_components=2, random_state=42, perplexity=5)
tsne_result = tsne.fit_transform(X)


plt.figure(figsize=(8, 6))
for i in range(num_clusters):
    plt.scatter(tsne_result[labels == i, 0], tsne_result[labels == i, 1], label=f"Cluster {i}")


for i, word in enumerate(words):
    plt.text(tsne_result[i, 0] + 0.02, tsne_result[i, 1] + 0.02, word, fontsize=9)

plt.title("Word Clusters using Word2Vec and t-SNE")
plt.legend()
plt.show()
