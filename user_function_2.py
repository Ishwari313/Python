def multiplication(value1, value2):
    ans = 0 #local variable because it is in inside the function
    ans = value1 * value2  #business logic (actual logic)
    return ans

print("Demo Application")

no1 =10
no2 = 11
result = 0

result=multiplication(no1,no2)
print("Multiplication is:",result)
