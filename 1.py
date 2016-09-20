xs = [14.3,15.3,14.1,14.3,14.8,15.6,14.8,15.6,15.2,15.8,
		14.3,16.1,14.5,13.3,14.3,13.9,14.6,14.1,16.4,15.2,14.1,
		15.4,16.9,14.4,14.3,15.2,14.2,14,16.1,15.2,16.9,14.4,13.1,
		15.9,14.9,13.7,15.5,16.5,15.2,13.8,12.6,14.8,14.4,15.6,14.6,
		15.1,15.2,14.5,14.3,17,14.6,12.8,15.4,14.9,16.4,16.1,15.2,
		14.8,14.2,16.6,16.8,14,15.7,15.6,
		]

xs1 = "VOVVAOVOVGOVAVGPVOGAVVOGOVVAGOVPVOOGOOVAGAOVOOGVAGGG"
ys1 = []
for i in xs1:
	ys1.append(i)
ys1.sort()

print(len(xs))

ys = []
for i in xs:
	ys.append(int(i*10))

print(ys)
print(len(ys))
ys.sort()
print(ys)

#busqueda en una lista de listas ordenada
def buscar(xs,x):
	if xs == []:
		return False
	for i in xs:
		if i[0] == x:
			return True
	return False

zs = []

for i in ys1:
	#print(zs)
	if not buscar(zs,i):
		zs.append([i,1])
	else:
		zs[-1][1] += 1

print(zs)
