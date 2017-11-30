# import picasso
# import numpy.random as r

# def linear_search(a, v):
#     for i in range(len(a)):
#     	if v == a[i]:
#     		return i

#     return -1

# a = [5, 4, 3, 2, 1]
# print linear_search(a, 1)

# p = picasso.Picasso('linear_search')
# p.draw_best_fitting_line = True
# for i in range(0, 15001, 1000):
#     p.start(i)
#     a = r.random_integers(0, i, i)
#     linear_search(a, 1)
#     p.end()
#     p.export()




def binary_search(a, v):
	first = 0
	last = len(a)-1
	number = False
	while( first<=last and not number):
		mid = (first + last)/2
		if a[mid] == v :
			found = True
		else:
			if v < a[mid]:
				last = mid -1
			else:
				first = mid + 1	
	return number 
a = [1, 2, 3, 4, 5]
print v