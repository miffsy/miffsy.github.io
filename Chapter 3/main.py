import math

print("1.1:\n")
a = [1,5,"meow","nya"]
print("List a: ",a)
print("Visual reversal: ",a[::-1])
a.reverse()
print("Actual reversal: ",a)
a.reverse()
print("Flipped to original: ",a)
print("\n")

print("1.2:\n")
b = [1,2,3,4,5,6,7]
print("List b: ",b)
for i in range(len(b)):
    b[i] = b[i] * b[i]
print("List b squared: ",b)
print("\n")

print("1.3:\n")
c = ["Bingus","Miette"]
d = ["Courage","Scooby Doo"]
e = []
print("List c: ",c)
print("List c:", d)
for itrt1 in range(len(c)):
    for itrt2 in range(len(d)):
        e.append(c[itrt1]+" "+d[itrt2])
print("Concatenated:",e)        
print("\n")

print("2.1a:\n")
f = [10, -10, 5, 2, 8, -2]
print("List f: ",f)
j = len(f)
for g in range(j-1):
        for h in range(0, j-g-1):
            if f[h] > f[h + 1]:
                f[h], f[h + 1] = f[h + 1], f[h]
print("The largest sum is:", (f[j-1] + f[j-2]))
print("\n")

print("2.1b:\n")
k = [10, -10, 5, 2, 8, -2]
print("List k: ",k)
l = len(k)
o = []
for m in range(l-1):
        for n in range(0, l-m-1):
            if k[n] > k[n + 1]:
                k[n], k[n + 1] = k[n + 1], k[n]
                o.append(math.pow(k[n], k[n + 1]))
p = len(o)
for q in range(p-1):
        for r in range(0, p-q-1):
            if o[r] > o[r + 1]:
                o[r], o[r + 1] = o[r + 1], o[r]

print("List k's powers (roughly): ",o)
print("The largest power is:", (o[p-1]))
print("\n")

print("2.2:\n")
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = 4
print("List s: ",s,"Amount t:",t)
u = len(s)
for v in range(t):
    s.insert(0,s.pop(u-1))
print("List s rotated by t amount: ",s)   
print("\n")

print("2.3:\n")

w = [1, [2, [3, 4], [5]], 6]
x = []
print("List w to be flattened",w)
def unnester(w):
     for y in w:
        if type(y) == list:
            unnester(y)
        else:
            x.append(y)
unnester(w)
print("Flattened list: ",x)
print("\n")