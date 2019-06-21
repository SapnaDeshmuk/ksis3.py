marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
i=0
max=0
while i<len(marks):
	marks1=len(marks[i])
	j=0
	while j<(marks1):
		print marks[i][j]
		j=j+1
		max=max+i
	i=i+1
	print"**********"