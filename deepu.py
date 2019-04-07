#deepu.py
l=[]
for i in range (1000,10000):
    if(i%15==0)and(i%21==0)and(i%28==0):
        l.append(i)
    else:
        pass
l.sort()
n=len(l)
print(l[n-1])
        
