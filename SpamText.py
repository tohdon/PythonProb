# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:52:11 2021

@author: user
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline, make_pipeline

from sklearn.feature_extraction.text import TfidfTransformer

d = pd.read_csv(r'C:\Temp\node\YouTube-Spam-Collection-v1\Youtube01-Psy.csv')
print(d.tail)
vectorizer = CountVectorizer()
dvec = vectorizer.fit_transform(d['CONTENT'])
print(vectorizer.get_feature_names())
dshuf = d.sample(frac=1)
d_train = dshuf[:300]
d_test = dshuf[300:]
d_train_att = vectorizer.fit_transform(d_train['CONTENT'])
d_test_att = vectorizer.transform(d_test['CONTENT'])
d_train_label = d_train['CLASS']
d_test_label = d_test['CLASS']

clf = RandomForestClassifier(n_estimators=80)
clf.fit(d_train_att, d_train_label)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                       max_depth=None, max_features='auto', max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None, 
                       min_samples_leaf=1,min_samples_split=2, 
                       min_weight_fraction_leaf=0.0, n_estimators=80, n_jobs=1,
                       oob_score=False, random_state=None, verbose=0, warm_start=False)
wclfscore = clf.score(d_test_att,d_test_label)

print("score: " + str(wclfscore))

pred_labels = clf.predict(d_test_att)
wconfus= confusion_matrix(d_test_label, pred_labels)
print("confustion matrix")
print(wconfus)

scores = cross_val_score(clf, d_train_att, d_train_label, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))

d= pd.concat([ pd.read_csv(r'C:\Temp\node\YouTube-Spam-Collection-v1\Youtube01-Psy.csv'),
               pd.read_csv(r'C:\Temp\node\YouTube-Spam-Collection-v1\Youtube02-KatyPerry.csv'),
               pd.read_csv(r'C:\Temp\node\YouTube-Spam-Collection-v1\Youtube03-LMFAO.csv'),
               pd.read_csv(r'C:\Temp\node\YouTube-Spam-Collection-v1\Youtube04-Eminem.csv'),
               pd.read_csv(r'C:\Temp\node\YouTube-Spam-Collection-v1\Youtube05-Shakira.csv')
            ])
print("Total Files data:" + str(len(d)))
dshuf = d.sample(frac=1)
d_content = dshuf['CONTENT']
d_label = dshuf['CLASS']
pipeline = Pipeline([
            ('bag-of-words', CountVectorizer()),
            ('random forest', RandomForestClassifier()),
            ])

print(pipeline)
pipeline = make_pipeline(CountVectorizer(), RandomForestClassifier())

pipeline.fit(d_content[:1500], d_label[:1500])
wpipscore = pipeline.score(d_content[:1500], d_label[:1500])

print("pipline score")
print(str(wpipscore))
pipeline.predict(["what a neat video!"])
pipeline.predict(["plz subscribe to my channel!"])
scores = cross_val_score(pipeline, d_content, d_label, cv=5)
print("Cross validate Accuracy with RandomForest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))


pipeline2 = make_pipeline(CountVectorizer(), TfidfTransformer(norm=None),RandomForestClassifier() )
scores = cross_val_score(pipeline2, d_content, d_label, cv=5)
print("Cross validate Accuracy with TF-IDF: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))

