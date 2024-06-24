import sys
sys.path.append('/path/to/site-packages')
print("Sys is running here",sys.executable)
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='ticks',color_codes=True)
titanic = sns.load_dataset('titanic') #We already have titanic data in our sns model
graph = sns.FacetGrid(titanic,row='sex', hue= 'alone')  
# g = (graph.map(plt.scatter, 'age', 'fare').add_legend())
# g = sns.catplot(x= 'sex', y='survived', hue='class' , kind='bar', data=titanic) # Hue = color, kind= chart type, data we will tell the csv data
g = sns.countplot(x= 'sex', hue='class' , data=titanic) # Hue = color, kind= chart type, data we will tell the csv data
g.set_title("Titanic Graph")
plt.show()