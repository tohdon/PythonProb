
from sklearn.ensemble import BaggingClassifier
log_reg_for_bagging = LogisticRegression()

bagging = BaggingClassifier(base_estimator=log_reg_for_bagging, n_estimators=10, random_state=55, n_jobs=-1)

bagging.fit(x_train, y_train) 
y_pred_test = bagging.predict(x_test)
metrics.loc['accuracy','bagging'] = accuracy_score(y_pred=y_pred_test, y_true=y_test)
metrics.loc['precision','bagging'] = precision_score(y_pred=y_pred_test, y_true=y_test)
metrics.loc['recall','bagging'] = recall_score(y_pred=y_pred_test, y_true=y_test)
CM = confusion_matrix(y_pred=y_pred_test, y_true=y_test)
vcm = CMatrix(CM)
print(vcm)
