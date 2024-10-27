l=int(input("Enter The Length: "))
b=int(input("Enter The Breadth: "))
print("* "*b)
for i in range(1,l-1):
    print("*"+" "*((b*2)-3)+"*")
print("* "*b)


