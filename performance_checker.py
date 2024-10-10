def get_even_odd_count1(L):
    even, odd = 0, 0
    for ele in L:
        if ele % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def eo_1():
    return get_even_odd_count1(list(range(1, 100000)))  # Increased list size

def get_even_odd_count2(L):
    even, odd = 0, 0
    for ele in L:
        t = ele % 2
        even += 1 - t
        odd += t
    return even, odd

def eo_2():
    return get_even_odd_count2(list(range(1, 100000)))  # Increased list size

def get_even_odd_count3(L):
    odd = 0
    for ele in L:
        odd += ele % 2
    return len(L) - odd, odd

def eo_3():
    return get_even_odd_count3(list(range(1, 100000)))  # Increased list size

import time

def check_performance3(approaches):
    time_taken = []
    for approach in approaches:
        time_take = []
        for _ in range(1000):  # Increased the number of iterations
            start_time = time.time()
            approach()
            end_time = time.time()
            time_take.append(end_time - start_time)
        time_taken.append(sum(time_take) / 1000)  # Average over 1000 iterations
    return time_taken

# Measure the performance of each approach
print(check_performance3([eo_1, eo_2, eo_3]))
