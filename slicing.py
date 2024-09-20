import time
import random

def check_fun(arr):
    for num in arr:
        i = int(num)

def check_opr(arr):
    for num in arr:
        i = num//1

def check_speed(approaches,arr):
    spec_times=[]
    for approach in approaches:
        start_time = time.time()
        for _ in range(100):
            approach(arr)
        end_time = time.time()
        spec_times.append((end_time-start_time)/100)
    return list(zip(approaches, spec_time))
    
def generate_random(limit):
    nums = []
    for i in range(limit):
        nums.append(random.random()*random.random()*1000)
    return nums
    
arr = generate_random(1000)    
print(check_speed([check_fun(arr), check_opr(arr)],arr))

        
        
        
        
        
        



