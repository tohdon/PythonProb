rfprobas = RF.predict_proba(x_test)[:, 1]
lrprobas = log_reg.predict_proba(x_test)[:, 1]  
precision_rf, recall_rf, thresholds_rf = precision_recall_curve(y_true=y_test, probas_pred=rfprobas)
precision_lr, recall_lr, thresholds_lr = precision_recall_curve(y_true=y_test, probas_pred=lrprobas)

fig,ax = plt.subplots(figsize=(8,5))
ax.plot(precision_rf, recall_rf, thresholds_rf, label='Random Forest')
ax.plot(precision_lr, recall_lr, thresholds_lr, label='Logistic Regression')
ax.set_ylim(0.5,1)
ax.set_xlim(0.2,0.6)
ax.set_ylabel('Recall')
ax.set_xlabel('Precision')
ax.set_title('Random Forest vs Logistic Regression')
ax.legend()
ax.grid()

