# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:18:11 2021

@author: Don
"""
import pandas as pd
import numpy as np
from sklearn import tree 
import matplotlib.pyplot as plt
from dtreeviz.trees import *
from sklearn.model_selection import cross_val_score

d = pd.read_csv(r'C:\software\python\student\student-por.csv', sep=';')
print(len(d))

d['pass'] = d.apply(lambda row: 1 if (row['G1'] + row['G2'] + row['G3']) >= 35 else 0, axis=1)
d = d.drop(['G1', 'G2','G3'] , axis=1)
print(d.head())
d = pd.get_dummies(d, columns = ['sex','school', 'address', 'famsize',
                                'Pstatus', 'Mjob', 'Fjob','reason', 
                                'guardian','schoolsup','famsup','paid','activities',
                                'nursery','higher','internet','romantic'])
print(d.head())

d = d.sample(frac =1)

d_train = d[:500]
d_test = d[500:]
d_train_att = d_train.drop(['pass'], axis=1)
d_train_pass = d_train['pass']
d_att = d.drop(['pass'], axis=1)
d_pass = d['pass']

print("Passing %d out of %d (%.2f%%)" % (np.sum(d_pass), len(d_pass), 100*float(np.sum(d_pass))/ len(d_pass)))
t = tree.DecisionTreeClassifier(criterion= "entropy", max_depth=5)
t = t.fit (d_train_att, d_train_pass)
tree.export_graphviz(t, out_file="student-perf.dot", label="all", impurity=False, propertion=True, feature_names=list(d_train_att), class_names=['fail','pass'], filled=True, rounded = True)
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:18:11 2021
@author: Don
"""
import pydot
import pandas as pd
import numpy as np
from sklearn import tree 
import matplotlib.pyplot as plt
from dtreeviz.trees import *
d = pd.read_csv(r'student-por.csv', sep=';')
print(len(d))

d['pass'] = d.apply(lambda row: 1 if (row['G1'] + row['G2'] + row['G3']) >= 35 else 0, axis=1)
d = d.drop(['G1', 'G2','G3'] , axis=1)
print(d.head())
d = pd.get_dummies(d, columns = ['sex','school', 'address', 'famsize',
                                'Pstatus', 'Mjob', 'Fjob','reason', 
                                'guardian','schoolsup','famsup','paid','activities',
                                'nursery','higher','internet','romantic'])
print(d.head())

d = d.sample(frac =1)

d_train = d[:500]
d_test = d[500:]
d_train_att = d_train.drop(['pass'], axis=1)
d_train_pass = d_train['pass']
d_att = d.drop(['pass'], axis=1)
d_pass = d['pass']

print("Passing %d out of %d (%.2f%%)" % (np.sum(d_pass), len(d_pass), 100*float(np.sum(d_pass))/ len(d_pass)))
t = tree.DecisionTreeClassifier(criterion= "entropy", max_depth=5)
t = t.fit (d_train_att, d_train_pass)
tree.export_graphviz(t, out_file="C:\\tmp\\node\\student-perf.dot", label="all", impurity=False, proportion=True, feature_names=list(d_train_att), class_names=['fail','pass'], filled=True, rounded = True)
viz = dtreeviz(t, 
               x_data=d_train_att,
               y_data=d_train_pass,
               target_name='pass',
               feature_names=list(d_train_att), 
               class_names=['fail','pass'], 
               title="Decision Tree - Student Result data set")
viz.save(r'D:\student.svg') # suffix determines the generated image format
viz.view()             # pop up window to display image
wtscore = t.score(d_test_att, d_test_pass)

print("tscore:" + str(wtscore))

scores = cross_val_score(t, d_att, d_pass, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2 ))

for max_depth in range(1,30):
    t = tree.DecisionTreeClassifier(criterion= "entropy", max_depth=max_depth)
    scores = cross_val_score(t, d_att, d_pass, cv=5)
    print("Max Depth: %d Accuracy: %0.2f (+/- %0.2f)" % (max_depth, scores.mean(), scores.std()*2 ))

depth_acc = np.empty((19,3), float)
i = 0
for max_depth in range(1,20):
    t = tree.DecisionTreeClassifier(criterion= "entropy", max_depth=max_depth)
    scores = cross_val_score(t, d_att, d_pass, cv=5)
    depth_acc[i,0] = max_depth
    depth_acc[i,1] = scores.mean()
    depth_acc[i,2] = scores.std() *2
    i +=1
    
fig,ax = plt.subplots()

ax.errorbar(depth_acc[:,0],depth_acc[:,1],yerr=depth_acc[:,2])    
plt.show()
