'''
l=[1,2,3,4,5,6]
k={}
for i in range(len(l)):
    if i%2==0:
        k.update({l[i]:l[i+1]})
print(k)

l=[1,2,3,4,5,6]
j=[]
k=[]
for i in l:
    if i%2==0:
        j.append(i)
    else:
        k.append(i)

print(dict.fromkeys(k,j))

l=[1,2,3,4,5,6]
k={}
for i in range(len(l)):
    if i%2==0:
        k.update({l[i]:l[i+1]})
print(k)

l=[1,2,3,4]
k=[4,5,6,7]
print(dict(zip(l,k)))

l=[12,54,85,482,25]
j=[]
k=[]
for i in l:
    if i%2==0:
        j.append(i)
    else:
        k.append(i)
print(dict(zip(k,j)))

l=[12,54,85,482,25,512]
j=[]
k=[]
for i in range(len(l)):
    if i%2==0:
        j.append(l[i])
    else:
        k.append(l[i])
print(dict(zip(k,j)))

l='hello juber how are you'
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)

l=[1,2,3,4,252,6]
for i in range(len(l)):
    print(i)

l=[1,2,3,4]
for i in range(len(l)):
    print(l[i])
'''



