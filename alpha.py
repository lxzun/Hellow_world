import string
stri = input("Tipe!\n--> ")
dis_l = [c for c in string.ascii_lowercase]
dis_u = [c for c in string.ascii_uppercase]
dis = [0]*len(string.ascii_uppercase)

for W, w in zip(dis_u,dis_l):
	i = dis_l.index(w)
	dis[i] += stri.count(W)
	dis[i] += stri.count(w)

for n, W in zip(dis, dis_u):
	print(W + ' ' + '#'*n)