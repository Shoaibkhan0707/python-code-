l=[1,2,3,4,1,2,3,4,5,6,7]
i=0
j=0
for i in range(len(l)):
        for j in range(len(l)):
                if l[i]==l[j]:
                        break
        if(i==j):
                print(l[j])

