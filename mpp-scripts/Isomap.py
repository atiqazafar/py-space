import pandas as pd
import numpy as np
import scipy.io
import random, math

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def Plot2D(T, title, x, y, num_to_plot=40):
  # This method picks a bunch of random samples to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
  for i in range(num_to_plot):
    img_num = int(random.random() * num_images)
    x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
    x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
    img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7)



# A .MAT file is a .MATLAB file. 
mat = scipy.io.loadmat('E:/Study/MPPData/Python/DAT210x-master/Module4/Datasets/face_data.mat')
df = pd.DataFrame(mat['images']).T
num_images, num_pixels = df.shape
num_pixels = int(math.sqrt(num_pixels))

# Rotate the pictures, so we don't have to crane our necks:
for i in range(num_images):
  df.loc[i,:] = df.loc[i,:].reshape(num_pixels, num_pixels).T.reshape(-1)


#
# PCA: Reduce the dataframe df down to THREE components.
from sklearn.decomposition import PCA
pca = PCA(n_components=3, svd_solver='full')
pca.fit(df)
T = pca.transform(df)

#
# The format is: Plot2D(T, title, x, y, num_to_plot=40):
# T is your transformed data, NDArray.
# title is your chart title
# x is the principal component you want displayed on the x-axis, Can be 0 or 1
# y is the principal component you want displayed on the y-axis, Can be 1 or 2
Plot2D(T, "PCA Plot", 0, 1, num_to_plot=40)

# Isomap: Reduce the dataframe df down to THREE components.
from sklearn import manifold
iso = manifold.Isomap(n_neighbors=4, n_components=2)
iso.fit(df)
Y = iso.transform(df)

Plot2D(Y,'isomap',0,1)


plt.show()
