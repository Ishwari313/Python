class Demo:
    No = 10

    #instance method
    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside instance method fun:",self.Value1,self.Value2)

    #class method does not need to obj for accessing
    @classmethod 
    def sun(cls):
        print("Inside class method Sun:",cls.No)

Demo.sun()
print("class variable No : ",Demo.No)

obj = Demo(11,21)

obj.fun()

print("instance variable :",obj.Value1,obj.Value2)
