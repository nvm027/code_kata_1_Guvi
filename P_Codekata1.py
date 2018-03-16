flg=0
v1=[]
c=[]
d={}
j=0
a=int(input("Enter the Num:"))
for i in range(0,a):
    v1.append(input("Enter The String:"))
set1=set(v1)
b=set1.pop()
v1.remove(b)
b=list(b)
print(b)
print(v1)
while(j<len(b)):
    if flg==-1:
        break
    for i in v1:
        if b[j]==i[j]:
            flg=0
        else:
           flg=-1
            break
    if flg==0:
        c.append(b[j])
    j=j+1
c="".join(c)
print (c)
