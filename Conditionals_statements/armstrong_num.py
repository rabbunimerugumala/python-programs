num = int(input("Enter The Number: "))
sum = 0
leng = len(str(num))
n = num
while n > 0:
    digit = n % 10
    sum += digit**leng
    n //= 10
if num == sum:
    print(num, "Is An Amstrong Number..")
else:
    print(num, "Is Not An Amstrong Number..")
