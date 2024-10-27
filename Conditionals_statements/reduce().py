#    sum of first 100 natural numbers..

from functools import reduce


res = reduce(lambda x,y: x+y ,range(1,101))
print(res)


