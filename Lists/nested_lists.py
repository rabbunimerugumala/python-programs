rows =  int(input("Enter The Rows: "))
nlist = []
for _ in range(rows):
    data=input().split(" ")
    data= list(map(int,data))
    nlist.append(data)
print(nlist)
for sublist in nlist:
    print(sublist)
for slist in nlist:
    for val in slist:
        print(val,end=" ")

