#xs = [14.3,15.3,14.1,14.3,14.8,15.6,14.8,15.6,15.2,15.8,
#		14.3,16.1,14.5,13.3,14.3,13.9,14.6,14.1,16.4,15.2,14.1,
#		15.4,16.9,14.4,14.3,15.2,14.2,14,16.1,15.2,16.9,14.4,13.1,
#		15.9,14.9,13.7,15.5,16.5,15.2,13.8,12.6,14.8,14.4,15.6,14.6,
#		15.1,15.2,14.5,14.3,17,14.6,12.8,15.4,14.9,16.4,16.1,15.2,
#		14.8,14.2,16.6,16.8,14,15.7,15.6,
#		]

xs = [35.6,31,30,30.5,33.5,
    27.9,31.6,28.7,31.3,30.5,
    29.3,28,33.2,24.9,30.6,
    31.8,33.7,30.5,26.8,35.1,
    22.5,32,27.9,29.9,28.6,
    34.2,28.5,31.2,28.7,30.1,
    34.2,27.5,29.5,30.4,30.3,
    32.7,29.8,28.7,31.3,29.6,
    26.5,31.2,23,32.7,31.4,
    26.4,28.7,30.1,30.3,32.4]

xs1 = "VOVVAOVOVGOVAVGPVOGAVVOGOVVAGOVPVOOGOOVAGAOVOOGVAGGG"
ys1 = []
for i in xs1:
	ys1.append(i)
ys1.sort()

print(len(xs))

ys = []
for i in xs:
	ys.append(int(i*10))

#busqueda en una lista de listas ordenada
def buscar(xs,x):
	if xs == []:
		return False
	for i in xs:
		if i[0] == x:
			return True
	return False

zs = []

for i in xs:
	#print(zs)
	if not buscar(zs,i):
		zs.append([i,1])
	else:
		zs[-1][1] += 1

print(zs)

sum = 0
for i in zs:
    sum += i[1]
print(sum)

#for i in zs:
#    i[1] = round(float(i[1])/sum,4)
#print (zs)
#
#xs = [20,5.7,9.6,13.6,16.3,13.5,8.7,12.6]
#ys = [0]
#for i in xs:
#    ys.append(ys[-1]+i)
#print(ys)
