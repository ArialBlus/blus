from sklearn.neighbors import NearestNeighbors
import numpy as np


x_train=np.array([[1,2],[2,3],[3,4], [4,5], [5,6]])

x_unknow= np.array([[1.5, 2.5], [3.5, 4.5]])


model=NearestNeighbors(n_neighbors=2)
model.fit(x_train)

distance, indices=model.kneighbors(x_unknow)

for i in range (len(x_unknow)):
    print("para la observacion", x_unknow[i], "los vecinos mas cercanos son:", x_train[indices[i]])

