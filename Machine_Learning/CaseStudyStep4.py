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
