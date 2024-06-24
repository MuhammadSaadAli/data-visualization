import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np #Use Np before using the values of numpy such as mean median mode and many other
# Load Datasets

# flowers = sns.load_dataset('iris')
kashti = sns.load_dataset('titanic')
# print(flowers)

# Draw a line plot
# sns.barplot(x='class', y='fare', hue='sex', data=kashti, estimator=np.mean)
sns.barplot(x='class', y='fare', data=kashti, linewidth =3, errcolor='0.6', edgecolor='0', facecolor=(0.1,0.3,0.3,0.5) )
plt.title("titanic Bar plot")
plt.show()