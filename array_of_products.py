def arrayOfProducts(array):
	products = [1 for _ in range(len(array))]
	
	left_product = 1
	for pos in range(len(array)):
		products[pos] = left_product
		left_product *= array[pos]
		
	right_product = 1
	for pos in reversed(range(len(array))):
		products[pos] *= right_product
		right_product *= array[pos]
		
	return products
