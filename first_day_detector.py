''' For detecting first day of the year we use following formula :
            (Year code + Month code + Century Code + Date Number +(Leap Year code ))%7
            Year code = (last2digitofyear + (L2D /4))%7
            month code = 0 for Janaury
            Century code = 
            Date Number = 1 for 1st Jan
            leap code = 1 for jan
'''
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
century_code  = 6
Date_num = 1

days = ['Sun' , 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'  ]
day_value =  (year_code + month_code + century_code + Date_num - leap)%7
print(day_value)

no_of_days_in_month=[31,28+leap,31,30,31,30,31,31,30,31,30,31]
name_of_months=('Janaury' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July'  , 'August' , 'September' , 'October' , 'November' , 'December')


for j in range(0,12):
    print(name_of_months[j].center(40))
    for i in range(len(days)):
        print(days[i] , sep=' ' , end ='  ')
    print()

    for i in range(day_value):
        print(' ' , sep=' ' , end ='    ')
    curr=day_value        
    for i in range(1,no_of_days_in_month[j]+1):
        if i<10:
            print(i , sep=' ' , end ='    ')
        else:
            print(i , sep=' ' , end ='   ') 
        if (curr+i)%7==0:
            print()
    day_value=(curr+i)%7
    print()
    print()
    


    


