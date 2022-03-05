
from sklearn.ensemble import AdaBoostClassifier


boosting = AdaBoostClassifier( n_estimators=50, random_state=55, learning_rate=0.1)

boosting.fit(x_train, y_train) 
y_pred_test = boosting.predict(x_test)
metrics.loc['accuracy','boosting'] = accuracy_score(y_pred=y_pred_test, y_true=y_test)
metrics.loc['precision','boosting'] = precision_score(y_pred=y_pred_test, y_true=y_test)
metrics.loc['recall','boosting'] = recall_score(y_pred=y_pred_test, y_true=y_test)
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
vcm = CMatrix(CM)
print(vcm)