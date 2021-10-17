# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:18:11 2021

@author: Don
"""
import pandas as pd
import numpy as np
from sklearn import tree 
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