
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

data=pd.read_csv('/content/sample_data/mnist_test.csv')
data.head()

x = data.values[:,1:5]
y = data.values[:,0]

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=100)

clf_entropy = DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)
clf_entropy.fit(X_train,y_train)

y_pred_en = clf_entropy.predict(X_test)

print(accuracy_score(y_test,y_pred_en)*100)

