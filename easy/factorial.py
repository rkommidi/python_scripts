#/bin/env python

#Linear Way
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4))

#Recursive
def recursive_factorial(n):
	if n == 1:
	   return 1

	result = n * recursive_factorial(n-1)
	return result

print(recursive_factorial(4))

#divide and concur
def fact(start,end):

    if start == end:
        return end

    mid = (start + end ) // 2

    if mid == start:
        return (start * end)

    result = fact(start,mid) * fact(mid+1,end)
    return result


print(fact(1,4))
