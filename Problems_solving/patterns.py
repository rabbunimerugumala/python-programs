
#! RIGHT ANGLE TRIANGLE..

num = int(input("Enter Size Of The Pattern:-  "))

for i in range(0,num+1):
    spaces = " " * (num-i)   # 1-SPACE
    stars = "*" * i          # 1-STAR

    print(spaces+stars)

#TODO o/p:
#     *
#    **
#   ***
#  ****
# *****


# num = int(input("Enter Size Of The Pattern:-  "))
#
# for i in range(1,num+1):
#     spaces = "  " * (num-i)   # 2-SPACES
#     stars = "* " * i          # STAR AFTER SPACE
#
#     print(spaces+stars)

#   o/p:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# num = int(input("Enter Size Of The Pattern:-  "))
#
# for i in range(1,num+1):
#     spaces = " " * (num-i)     # 1-SPACE
#     stars = "* " * i           # STAR AFTER SPACE
#
#     print(spaces+stars)

#O/P:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# PYRAMIDS..

num = int(input("Enter Size Of The Pattern:-  "))

for i in range(1,num+1):

    spaces = "  " * (num-i)
    star = "* " * i
    rstar = "* " * (i-1)

    print( spaces + star + rstar)

# O/p:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *



# num = int(input("Enter Size Of The Pattern:-  "))
#
# for i in range(1,num+1):
#
#     spaces = "  " * (num-i)
#     stars = (str(i) + " ") * i
#     stars = (str(i)+" ") * (i - 1)
#
#     print( spaces + stars + stars)

#TODO: O/p:
#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5


num = int(input("Enter Size Of The Pattern:-  "))
for i in range(1,num+1):

    lspaces = " " * (num - i)

    if i > 2 and i < num :
        hollowspace = "  " * ( i - 2)
        stars = "* " + hollowspace + "*"
        print(lspaces + stars)

    else:
        stars = "* " * i
        print(lspaces + stars)

#TODO O/p:
#     *
#    * *
#   *   *
#  *     *
# * * * * *
