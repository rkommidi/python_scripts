
# O(2^n) time | O(n) space
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n-1) + getNthFib(n-2)



# O(n) time | O(n) space
def getNthFib(n, cache={1:0,2:1}):
	if n in cache:
		return cache[n]
	else:
		cache[n] = getNthFib(n-1,cache) + getNthFib(n-2, cache)
		return cache[n]
   

# O(n) and O(1)
def getNthFib(n):
	lastTwo = [0 ,1 ]
	counter = 3
	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1
		
	return lastTwo[1] if n > 1 else lastTwo[0]
		
