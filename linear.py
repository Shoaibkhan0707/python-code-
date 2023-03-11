l=[2,1,8,7,6,5,3]
se=2;
i=0
check=0;
while i<len(l):
    if l[i]==se:
        print("found")
        check=1
        break
    i=i+1
if check==0:
    print("not found")
