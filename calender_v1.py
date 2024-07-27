


l=list()
m=3
n=12//m
l.append(list(['0']*7))
for i in range(1,(m*7*n)+1):
    l.append(list(['0']*7))
    print(l[i] , sep=' ' , end ='   ')
    print('                ' , sep=' ' , end ='   ')
    if i%n==0:
        print()
    if i%(n*7)==0:
        print()
        print()
print()

month=['j','j','j','j','j','j','j','j','j','j','j','j']
day=['s','m','t','w','t','f','s']
print(len(l))

for i in range(1,len(l)):
    
    if i%(7*n)==1: 
        for j in range(n):
            l[i+j][4]=month[j]
    if i%(7*n)==n+1: 
        for j in range(n):
            for k in range(7):
                l[i+j][k]=day[k]
cur=1
newcur=0
for i in range(1,m+1):
    cur=newcur+1
    for j in range(1,n+1):
        
        newcur=cur+j-1
        print(newcur)
        for k in range(7):
            l[newcur][k]=j+(i-1)*n
            print(j+(i-1)*n)
            newcur+=n
       
    newcur-=n
            
            
    
            
            
print()
        















for i in range(1,(m*7*n)+1):
    
    print(l[i] , sep=' ' , end ='   ')
    print('                ' , sep=' ' , end ='   ')
    if i%n==0:
        print()
    if i%(n*7)==0:
        print()
        print()
print()
    
            
        
         
        
    



    
    






    


