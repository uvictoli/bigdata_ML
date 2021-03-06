# To load the decision tree classifier
from sklearn.tree import DecisionTreeClassifier

# To generate evaluation data for this classifier
from sklearn.model_selection import train_test_split

# To load the Iris Data Set
from sklearn import datasets

# For the basic mathematical/statistical operations
import numpy as np

# To draw plots
import matplotlib.pyplot as plt
import cp_utils as cpu

'''
Program Start
'''
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
tree.fit(X_train, y_train)

X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))

cpu.plot_decision_regions(X_combined, y_combined, classifier=tree, test_idx=range(105,150))

plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.show()

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=1, n_jobs=2)

forest.fit(X_train, y_train)

cpu.plot_decision_regions(X_combined, y_combined, classifier=forest, test_idx=range(105,150))

plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc='upper left')
plt.show()