bi = list(input("Input a binary number: "))
val = 0

for i in range(len(bi)):
	dig = bi.pop()
	if dig == '1':
		val = val + pow(2, i)
print("The decimal ", val)


