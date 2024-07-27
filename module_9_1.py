def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
        # results.setdefault(func.__name__,[]).append(func(int_list))
    return results

def max1(int_list):
    for i in int_list:
        return max(i)

def min1(int_list):
    for i in int_list:
        return min(i)

def len1(int_list):
    return len(int_list)

def sum1(int_list):
    return sum(int_list)

def sorted1(int_list):
    sor_ted = sorted(int_list)
    return sor_ted

#print(max([1,2,3,10]))
#print(min([1,2,3,10]))
#print(len1([1,2,3,10]))
#print(sum1([1,2,3,10]))
#print(sorted1([1,2,3,10]))

print(apply_all_func([2, 4 , 5, 6], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))