# num=int(input("Enter The Number: "))
# count=0
# for i in range(2,num):
#     if num % i == 0:
#         count+=1
#         break
# if count!=0:
#     print(num,"Is Not A Prime Number..")
# else:
#     print(num,"Is A Prime Number..")


num=int(input("Enter The Number: "))
for i in range(2,num):
    if num % i==0:
        print(f"{num} is not a prime..")
        break
else:
    print(f"{num} is prime number..")