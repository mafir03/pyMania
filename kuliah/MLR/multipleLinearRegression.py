import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import scipy.stats as stats
import seaborn as sns
import sklearn

path = 'realtor-data.csv'
df = pd.read_csv(path)
cdf = df[['bed', 'bath', 'acre_lot', 'house_size', 'price']].copy()

# filling in null values
cdf.bed.fillna(cdf.bed.mode()[0], inplace=True)
cdf.bath.fillna(cdf.bath.mode()[0], inplace=True)
cdf.acre_lot.fillna(cdf.acre_lot.mode()[0], inplace=True)
cdf.house_size.fillna(cdf.house_size.mode()[0], inplace=True)
print(cdf.shape)
z_score = np.abs(stats.zscore(cdf))
cdf_clean = cdf[(z_score<3).all(axis=1)]


# plt.scatter(cdf.bed, cdf.price, color='blue')
# plt.xlabel('house_size')
# plt.ylabel('price')
# plt.show()
