#Accept : multiple Parameters
#return: one value
def Marvellous1(value1,value2):
    print("inside marvellous1:",value1,value2)
    return 11

def main():
    result = None
    result = Marvellous1("python",21)
    print("Return value is :",result)


if __name__ == "__main__":
    main()