import seaborn as sns
import matplotlib.pyplot as plt

#Canva style
sns.set_theme(style='whitegrid')

kashti = sns.load_dataset('titanic')

sns.boxenplot(x ='class', y ='fare', data=kashti)
plt.show()