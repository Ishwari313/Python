def main():
    size = 0
    value =0

    print("Enter the number of elements:")
    size = int(input())

    Data = list()

    print("Enter the elements")

    for i in range(size):
        value =int(input())
        Data.append(value)


    print(Data)


if __name__ =="__main__":
    main()