
import sklearn

def main():
    print("Ball Classification Case Study")

   
    # Dataset Size 15
    # Feature Encoding
    Features  = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],
                [35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],
                [95,0]]
    
    #Label Encoding
    # Cricket = 2
    # Tennis = 1
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #features and labels should be numeric so we have to it encoding
    # Rough = 1
    # Smooth = 0
    # Called as one hot encoding
    
if __name__ =="__main__":
    main()