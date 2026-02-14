import sys

def main():
    print("Coomand line Arguments Are: ")

    for i in range(len(sys.argv)):
        print(sys.argv[i])
        
if __name__ =="__main__":
    main()