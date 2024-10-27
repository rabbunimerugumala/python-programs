n = int(input("Enter The Number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial Of", n, "Is", fact)

# OUTPUT..
# Enter The Number: 7
# Factorial Of 7 Is 5040


# iteration	   factorial*i (returned value)
# i = 1	        1 * 1 = 1
# i = 2	        1 * 2 = 2
# i = 3	        2 * 3 = 6
# i = 4	        6 * 4 = 24
# i = 5	       24 * 5 = 120
# i = 6	      120 * 6 = 720
# i = 7	      720 * 7 = 5040
