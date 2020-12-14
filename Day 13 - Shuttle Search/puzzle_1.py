dep=1005162
notes = "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13"

print("Solution 1:")
for n in notes.split(","):
	if not n == "x":
		n=int(n)
		print(n, n-(dep%n))

print("---")

print("Solution 2:")
offset = 0
ni = []
bi = []
for n in notes.split(","):
	if not n == "x":
		bi.append(int(n)-offset)
		ni.append(int(n))
	offset += 1

N = 1
for n in ni:
	N=n*N

Ni = [int(N/x) for x in ni]
xi = []
for count, n in enumerate(ni):
	i = 0
	x = 0
	while not x == 1:
		x = (Ni[count]*i)%ni[count]
		i += 1
	xi.append(i-1)


prod = []
for i in range(0, len(Ni)):
	print(bi[i], Ni[i], xi[i], (Ni[i]*bi[i]*xi[i]))
	prod.append(Ni[i]*bi[i]*xi[i])
	
print(sum(prod)%N)
