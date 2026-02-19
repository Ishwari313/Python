def main():
    try:
        open("Hello.txt","w")
        print("file gets Successfully open.")

    except FileNotFoundError:
        print("Unable to open as there is no such file.")

    finally:
        print("End of Application.")
        
if __name__ =="__main__":
    main()