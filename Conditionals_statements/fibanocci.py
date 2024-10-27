n = int(input("Enter The Number: "))
f1, f2 = 0, 1
for i in range(0, n):
    f = f1 + f2
    print(f, end="\t")
    f1, f2 = f2, f
