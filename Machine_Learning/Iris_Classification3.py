from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")

    Dataset = load_iris()

    # Meta data of dataset
    print("Independant Variables are :")
    print(Dataset.feature_names)
    print("Length of Independent variable is :",len(Dataset.feature_names))

    print("Dependent Variables are :")
    print(Dataset.target_names)
    print("Length od dependent varibales is :",len(Dataset.target_names))


    print(Dataset)

if __name__=="__main__":
    main()