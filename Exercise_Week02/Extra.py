print("ADDITION")
x=int(input("First Number: "))
y=int(input("Second Number: "))
output=str(x+y)
print(str(x) +  " + " + str(y) + " = " + output)

print("SUBTRACTION")
x=int(input("First Number: "))
y=int(input("Second Number: "))
output=str(x-y)
print(str(x) +  " - " + str(y) + " = " + output)


print("MULTIPLICATION")
x=int(input("First Number: "))
y=int(input("Second Number: "))
output=str(x*y)
print(str(x) +  " * " + str(y) + " = " + output)


print("DIVISION")
x=int(input("First Number: "))
y=int(input("Second Number: "))
output=str(x/y)
print(str(x) +  " / " + str(y) + " = " + output)


print("EXPONENTS")
x=int(input("First Number: "))
y=int(input("Second Number: "))
output=str(x**y)
print(str(x) +  " ** " + str(y) + " = " + output)

print("BOOLEAN OPERATORS")
x=int(input("First Number: "))
y=int(input("Second Number: "))
print(str(x) +  " > " + str(y) + " ? " + str(x>y))
print(str(x) +  " < " + str(y) + " ? " + str(x<y))
print(str(x) +  " == " + str(y) + " ? " + str(x==y))
print(str(x) +  " != " + str(y) + " ? " + str(x!=y))
print(str(x) +  " >= " + str(y) + " ? " + str(x>=y))
print(str(x) +  " <= " + str(y) + " ? " + str(x<=y))


print("LISTS")
numberlist = [0,1,2,3]
numberlist[0] = int(input("First Number: "))
numberlist[1] = int(input("Second Number: "))
numberlist[2] = int(input("Third Number: "))
numberlist[3] = int(input("Fourth Number: "))
print("NUMBER LIST: ")
print(numberlist)
x = int(input("Access Number List [0-3] only: "))
print("Number at index " + str(x) + " is " + str(numberlist[x]))

print("DICTIONARY")
NumberDictionary = {"R1": "10","R2": "8" ,"R3": "15"}
print(NumberDictionary)
print(NumberDictionary["R1"][0])