import time

def merge(x):
	left = 0
	right = len(x)
	middle = (right+1)/2
	if right==1:
		return x
	x1 = x[left:middle]
	x2 = x[middle:right]
	x1 = merge(x1)
	x2 = merge(x2)
	x_merged = []
	i = 0
	j = 0
	while((i < len(x1)) and (j < len(x2))):
		if x1[i] <= x2[j]:
			x_merged.append(x1[i]) 
			i += 1
		else:
			x_merged.append(x2[j])
			j += 1
	if (i==len(x1)):
		for k in range(j,len(x2)):
			x_merged.append(x2[k])
	else:
		for k in range(i,len(x1)):
			x_merged.append(x1[k])

	return x_merged

if __name__ == "__main__":
	theStartTime = time.time()
	x = raw_input("Enter the set of numbers to sort:")
	x = x.split()
	for i in range(0,len(x)):
		x[i] = int(x[i])
	print x
	y = merge(x)
	print "merged list", y
	print 'elapsed: ' + str(time.time() - theStartTime)