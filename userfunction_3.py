def multiplication(value1, value2):
    ans = 0 #local variable because it is in inside the function
    ans = value1 * value2  #business logic (actual logic)
    return ans



no1 = 0
no2 = 0
result = 0

no1=int(input("Enter First number:"))

no2 = int(input("ENter the second number:"))


result=multiplication(no1,no2)
print("Multiplication is:",result)

print("-"*50)

no1=int(input("Enter First number:"))

no2 = int(input("ENter the second number:"))


result=multiplication(no1,no2)
print("Multiplication is:",result)
