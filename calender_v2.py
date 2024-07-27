def return_cur_day(cur_day):
    if cur_day<10:
        return str(cur_day)+' '
    else:
        return str(cur_day)



l=list()
m=4
n=12//m
l.append(list(['0']*7))
for i in range(1,(m*8*n)+1):
    l.append(list(['  ']*7))
    

month=['j','j','j','j','j','j','j','j','j','j','j','j']
months=['Janaury' , "February" , 'March' , 'April' , 'May' , 'June' , 'July'  , 'August' , 'September' , 'October' , 'November' , 'December', 'October' , 'November' , 'December']
day=['s','m','t','w','t','f','s']
no_of_days_in_month=[31,30,31,30,31,28,31,30,31,30,31,31,30,31,30,31]


for i in range(1,len(l)):
    
    if i%(8*n)==1: 
        for j in range(n):
            l[i+j][4]=month[j]
    if i%(8*n)==n+1: 
        for j in range(n):
            for k in range(7):
                l[i+j][k]=day[k]

cur=1
newcur=0
day_value=5
index=day_value
flag=0

for i in range(1,m+1):
    cur=newcur+1
    for j in range(1,n+1):
        
        newcur=cur+j-1
        day_value=index
        cur_day=1
        flag=0
        
        for k in range(8):
            if k ==0:
                month=list(months[1])
                l[newcur]=month
            if k==1:
                l[newcur]=['s ','m ','t ','w ','t ','f ','s ']
            if k==2:
                for i in range(day_value):
                    l[newcur][i]='  '
                for i in range(day_value,7):
                    l[newcur][i]=return_cur_day(cur_day)
                    cur_day+=1
            if flag!=1:
                if k in [3,4,5,6,7]:
                    for i in range(7):
                        if cur_day>no_of_days_in_month[i]:
                            index=i
                            flag=1
                            break
                        else:
                            l[newcur][i]=return_cur_day(cur_day)
                            cur_day+=1
            newcur+=n  
    newcur-=n
            
print()

for i in range(1,(m*8*n)+1):
    
    for j in range(len(l[i])):
        print(str(l[i][j]) , sep=' ' , end ='  ')
    print('                ' , sep=' ' , end ='   ')
    if i%n==0:
        print()
    if i%(n*8)==0:
        print()
        print()
print()
    
          
        
         
        
    



    
    






    


