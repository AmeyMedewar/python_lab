''' For detecting first day of the year we use following formula :
            (Year code + Month code + Century Code + Date Number +(Leap Year code ))%7
            Year code = (last2digitofyear + (L2D /4))%7
            month code = 0 for Janaury
            Century code = 
            Date Number = 1 for 1st Jan
            leap code = 1 for jan
'''
import sys
# This is phase 1 Finding First day of the year 
def determine_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 1    
            else:
                return 0
        else:
            return 1
    else:
        return 0

var_year = input("Enter year ")
var_year = int(var_year)
leap = determine_leap(var_year)
year_code =((var_year%100) + ((var_year%100)//4))%7
month_code = 0
century_code  = (6 - ((var_year//100)%4)*2)
Date_num = 1

days = ['Sun' , 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'  ]
day_value =  (year_code + month_code + century_code + Date_num - leap)%7


# This is phase 2 asking user about the format in which they want calender 
rows=input("Select Number of Rows You want from \n 1\n 2 \n 3 \n 4 \n 6\n")
m=int(rows)

if m==5 or m<1 or m>6:
    print("Please Enter a Valid Number of Rows")
    sys.exit()
    
n=12//m

l=list()
l.append(list(['0']*7))
for i in range(1,(m*8*n)+1):
    l.append(list(['  ']*7)) #creating a empty calender 

def return_cur_day(cur_day):
    if cur_day<10:
        return str(cur_day)+' '
    else:
        return str(cur_day)

   

#Declaring Constants for Calender
months=[' JANAURY ', ' FEBRUARY', '  MARCH  ', '  APRIL  ', '    MAY    ', '   JUNE   ', '   JULY   ', '  AUGUST  ', 'SEPTEMBER', ' OCTOBER ', ' NOVEMBER', ' DECEMBER']
day=['s','m','t','w','t','f','s']
no_of_days_in_month=[31,28+leap,31,30,31,30,31,31,30,31,30,31]
cur=1
newcur=0
index=day_value
flag=0
cur_month=0

for i in range(1,m+1):
    cur=newcur+1
    for j in range(1,n+1):
        
        newcur=cur+j-1
        day_value=index
        cur_day=1
        flag=0
        
        for k in range(8):
            if k ==0:
                month=months[cur_month]
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
                        if cur_day>no_of_days_in_month[cur_month]:
                            index=i
                            flag=1
                            break
                        else:
                            l[newcur][i]=return_cur_day(cur_day)
                            cur_day+=1
            newcur+=n 
        cur_month+=1

             
    newcur-=n
            
print()

#printing Calender in desired format 
for i in range(1,(m*8*n)+1):
    
    for j in range(len(l[i])):
        print(l[i][j] , sep=' ' , end ='  ')
    print('                ' , sep=' ' , end ='   ')
    if i%n==0:
        print()
    if i%(n*8)==0:
        print()
        print()
print()
    
          
        
         
        
    



    
    






    


