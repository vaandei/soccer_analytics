# Not sure this will be useful to create a class for

#==================================================================================#
class ensemble:
    """

    """

    def __init__(self,X=0,labels=0,name='linear',rand=42):
        self.X = X
        self.labels = labels
        self.name = name
        self.model = []
        self.rand = rand

    def bagging(self,oob_val=False):
        from sklearn.ensemble import BaggingClassifier
        from sklearn.tree import DecisionTreeClassifier
        self.model = BaggingClassifier(
            DecisionTreeClassifier(), n_estimators=500,
            max_samples=100, bootstrap=True, n_jobs=-1, oob_score_=oob_val)

        return(self.model)

    def bag_rand_forest(self):
        bag_clf = BaggingClassifier(
            DecisionTreeClassifier(max_features="auto", max_leaf_nodes=16),
            n_estimators=500, max_samples=1.0, bootstrap=True, n_jobs=-1)

    def oob_score(self):
        val = self.model.oob_score_
        return(val)

    def predictor(self,predict_val):
        return_val = self.model.predict(predict_val)
        return(return_val)

    def predict_percent(self,predict_val):
        pred_percent = self.model.predict_proba(predict_val)

    def predict_scores(self,predict_val):
        scores = self.model.decision_function(predict_val)
        return(scores)

    def accuracy(self,test,x_test,y_test):
        from sklearn.metrics import accuracy_score
        self.model.fit(self.X, self.labels)
        y_pred = self.model.predict(x_test)
        val = accuracy_score(y_test, y_pred)
        return accuracy_score(y_test, y_pred)

#==================================================================================#

from sklearn.tree import export_graphviz
f = open("pathway_scores.dot", 'w')
export_graphviz(
        tree_clf,
        out_file=f,
        feature_names=['Length','Num'],
        class_names=['Bad','Good'],
        rounded=True,
        filled=True
    )


# Voting classifier
log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
svm_clf = SVC()

voting_clf = VotingClassifier(
    estimators=[('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf)],
    voting='hard')
voting_clf.fit(X_train, y_train)




# Feature importance
for name, score in zip(iris["feature_names"], rnd_clf.feature_importances_):
    print(name, score)


# Lots of boosting stuff that I may add later, Chapter 7 Hands-On


#==================================================================================#
def plot_decision_boundary(clf, X, y, axes=[-1.5, 2.45, -1, 1.5], alpha=0.5, contour=True):
    x1s = np.linspace(axes[0], axes[1], 100)
    x2s = np.linspace(axes[2], axes[3], 100)
    x1, x2 = np.meshgrid(x1s, x2s)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    y_pred = clf.predict(X_new).reshape(x1.shape)
    custom_cmap = ListedColormap(['#fafab0','#9898ff','#a0faa0'])
    plt.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)
    if contour:
        custom_cmap2 = ListedColormap(['#7d7d58','#4c4c7f','#507d50'])
        plt.contour(x1, x2, y_pred, cmap=custom_cmap2, alpha=0.8)
    plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo", alpha=alpha)
    plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bs", alpha=alpha)
    plt.axis(axes)
    plt.xlabel(r"$x_1$", fontsize=18)
    plt.ylabel(r"$x_2$", fontsize=18, rotation=0)


def plot_regression_predictions(tree_reg, X, y, axes=[0, 1, -0.2, 1], ylabel="$y$"):
    x1 = np.linspace(axes[0], axes[1], 500).reshape(-1, 1)
    y_pred = tree_reg.predict(x1)
    plt.axis(axes)
    plt.xlabel("$x_1$", fontsize=18)
    if ylabel:
        plt.ylabel(ylabel, fontsize=18, rotation=0)
    plt.plot(X, y, "b.")
    plt.plot(x1, y_pred, "r.-", linewidth=2, label=r"$\hat{y}$")
#==================================================================================#