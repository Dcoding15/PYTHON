# Definition: Binary classification where we use sigmoid function, that takes input as independent variables and produces a probability value between 0 and 1.

# Assumptions: -
# 	1. No correlation between input variables.
# 	2. Only two dependent variable allowed.
# 	3. Linear relationship between independent variable and log odds of dependent variable.
# 	4. No outliers in datasets.
# 	5. Large sample size.
# 	6. Range of dependent variable is from 0 to 1 (y-axis).
# 	7. Range of independent variable is from -inf to inf (x-axis).
# 	8. Used only two dependent variable. We use softmax function if there are more than two variable.

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load the breast cancer dataset
X, y = load_breast_cancer(return_X_y=True)

# split the train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
# LogisticRegression
clf = LogisticRegression(random_state=0)
clf.fit(X_train, y_train)

# Prediction
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("Logistic Regression model accuracy (in %):", acc*100)
