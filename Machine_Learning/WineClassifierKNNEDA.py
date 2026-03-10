import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousClassifier(datapath):

    border ="-"*50

    #step 1:Load the dataset from the csv file

    print(border)
    print("Step 1: Load the dataset from csv file")
    print(border)

    df=pd.read_csv(datapath)

    print(border)
    print("Some entries from dataseer")
    print(df.head())
    print(border)

    # Step 2:clean the dataset by removing empty rows

    print(border)
    print("Step 2: Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace = True)
    print("Total records :",df.shape[0])
    print("Total columns :",df.shape[1])
    print(border)

    #step 3 Separate Independent and Dependent Variables

    print(border)
    print("Step 3 : Seperate Independent and Dependent Variables")

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X:",X.shape)
    print("Shape of Y :",Y.shape)

    print(border)
    print("Input columns:",X.columns.to_list())
    print("Output columnn : Class")


def main():

    border = "-"*60

    print(border)
    print("Wine Classfier Using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")



if __name__ == "__main__":
    main()