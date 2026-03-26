import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Step 1: Load the dataset

df = pd.read_csv("Breast_Cancer.csv")
print("Shape of dataset:",df.shape)
print("First 5 records:",df.head())

# Step 2 :Separate features and labels

X = df.drop("target",axis=1)

Y = df["target"]

#  Step 3 :Split the dataset for training and testing

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

# Step 4 : Create boosting model(Ada boost)

boost_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42,
    learning_rate=1.0
    )
# Step 5: Training Boosting model

boost_model.fit(X_train,Y_train)

# Step 6: Tst Bagging Model

y_pred = boost_model.predict(X_test)


# Step 7 : Evalute the Bagging Model

print("Bagging Accuracy : ",accuracy_score(Y_test,y_pred)*100,"%")

print()

print("Confusion Matrix :")
print(confusion_matrix(Y_test,y_pred))
