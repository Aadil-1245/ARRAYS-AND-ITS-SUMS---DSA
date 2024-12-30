# ARRAYS 
def fun(arr):
    largest_num = arr[0]
    for i in range (1,len(arr)):

        if arr[i] > largest_num:
            largest_num = arr[i]
    return largest_num
arr = [1,9,7,3,9]
print(fun(arr))