
from sklearn.ensemble import RandomForestClassifier


RF = RandomForestClassifier( n_estimators=10, random_state=55, max_features='sqrt', n_jobs=-1)

RF.fit(x_train, y_train) 
y_pred_test = RF.predict(x_test)
metrics.loc['accuracy','randomforest'] = accuracy_score(y_pred=y_pred_test, y_true=y_test)
metrics.loc['precision','randomforest'] = precision_score(y_pred=y_pred_test, y_true=y_test)
metrics.loc['recall','randomforest'] = recall_score(y_pred=y_pred_test, y_true=y_test)
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
vcm = CMatrix(CM)
print(vcm)