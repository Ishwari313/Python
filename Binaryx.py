Data=bytes([65,97,98])
print(type(Data))
print(Data)

print(Data[0]) #65
print(Data[1]) #97
Data[0]=66 # this give the error coz it is immutable

print(Data)