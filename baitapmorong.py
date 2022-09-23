j = []
for i in range(2000,3201):
	 if(i%7 ==0) and (i%5!=0):
	 	j.append(str(i))
print(','.join(j))
k = []
for e in range(999,4001):
	if(e%5==0) and (e%6==0):
		k.append(str(e))
print(','.join(k))

k = []
for e in range(999,4001):
	if(e%5==0) and (0<e%6<6):
		k.append(str(e))
print(','.join(k))


