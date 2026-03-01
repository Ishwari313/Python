import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import(

    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*50

#################################===============================###########################################
#                                    Step 1 : Load the dataset
#################################===============================###########################################

print()

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "Iris_Dataset.csv "

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial Entries from dataset : ")
print(df.head())

print()

#################################================================###########################################
#                                  Step 2 : Data Analysis (EDA)
#################################================================###########################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset :",df.shape)
print("Column Names:",list(df.columns))

print()

print("Missing values(per column) :")
print(df.isnull().sum())

print()

print("Class Distribution (Species Count)")
print(df["Species"].value_counts())

print()

print("Statistical Report of dataset :")
print(df.describe())

print()

#################################================================###########################################
#                                  Step 2 : Data Analysis (EDA)
#################################================================###########################################

print(Border)
print("Step 3 : Decides independent and dependent variables")
print(Border)

# X : Independent variables(features)
# Y : Dependent variables(labels)

feature_cols = [
    'SepalLength (Cm)',
    'SepalWidth (Cm)',
    'PetalLength (Cm)',
    'PetalWidth (Cm)'
]

X = df[feature_cols]
Y = df['Species']

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

print()

#################################==========================================###########################################
#                                   Step 4 : Visualization of Dataset
#################################===========================================###########################################

print(Border)
print("Step 4: Vissualization of Dataset")
print(Border)

print()

#scatter plot

plt.figure(figsize=(7,5))

for sp in df["Species"].unique():
    temp= df[df["Species"]==sp]
    plt.scatter(temp["PetalLength (Cm)"],temp["PetalWidth (Cm)"],label=sp)

plt.title("Iris: petal lengthh vs petal width")

plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")

plt.legend()
plt.grid(True)
plt.show()

print()


#################################=============================================###########################################
#                               Step 5 : Split the dataset for training and testing
#################################=============================================###########################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

print()

# Test size = 20%
# Train size = 80%

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.2, #OR train_size = 0.8
    random_state=42
)

print("Data splitting activity Done :")

print("X - Independent :",X.shape) #(150,4)
print("Y - Dependant :",Y.shape) #(150,)

print()

print("X_train :",X_train.shape) #(120,4)
print("X_test :",X_test.shape) #(30,4)

print()

print("Y_train :",Y_train.shape) #(120,)
print("Y_test :",Y_test.shape) #(30,)

print()


#################################=============================================###########################################
#                               Step 6 : Build the Model
#################################=============================================###########################################

print(Border)
print("Step 6: Build the Model")
print(Border)

print()

print("We are going to use DecisionTreeclassifier")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state = 42
)

print("Model successfully created:",model)

#################################=============================================###########################################
#                               Step 7 : Train the model
#################################=============================================###########################################

print(Border)
print("Step 7: Train the Model")
print(Border)

print()

model.fit(X_train,Y_train)
print("Model training completed....")

print()

#################################=============================================###########################################
#                               Step 8: Test the Model (Evaluate)
#################################=============================================###########################################

print(Border)
print("Step 8 : Test the Model")
print(Border)

print()

Y_pred = model.predict(X_test)

print("Model Evaluation (Testing) complete")

print(Y_pred.shape)

print("Expected answer :")
print(Y_test)

print("Prediced answer :")
print(Y_pred)