

"""
Project Euler #1: Multiples of 3 and 5

Sample Input 0

2
10
100

Sample Output 0

23
2318

"""
#code pattern simple
"""
import sys


def call_function(n):
    l1 = []
    sum = 0
    for i in range(2,n):
        print(i)
        if(i%3 == 0)or(i%5 ==0):
            print(i)
            l1.append(i)
            sum = sum + i
    print(sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    call_function(n)
"""

#code pattern complex

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = sum(x for x in list(filter(lambda x: ((x % 5 == 0)or(x%3 ==0)), range(2,n))))
    print(s)
