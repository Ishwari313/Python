#Accept : multiple Parameters
#return:  multiple value
def Marvellous1(value1,value2):
    print("inside marvellous1:",value1,value2)
    return 11,21,51

def main():
    result1 = None
    result2 = None
    result3 = None
    result1,result2,result3 = Marvellous1("python",21)
    print("Return value is :",result1,result2,result3)


if __name__ == "__main__":
    main()