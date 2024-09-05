import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


##################      Pré-processamento     ###################
# Coleta e Integração
iris = load_iris()

characteristics = iris.data

###################       Mineração        #####################
groups = KMeans(n_clusters=3, n_init=10, random_state=42)
groups.fit(X=characteristics)
labels = groups.labels_    # indice do grupo ao qual cada amostra pertence

################      Pós-processamento     ####################
fig = plt.figure(1)
ax = Axes3D(fig)
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(characteristics[:, 0], characteristics[:, 1], characteristics[:, 2], c=groups.labels_, edgecolor='k')

target = iris.target
fig = plt.figure(2)
ax = Axes3D(fig)
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(characteristics[:, 0], characteristics[:, 1], characteristics[:, 2], c=target, edgecolor='k')

plt.show()