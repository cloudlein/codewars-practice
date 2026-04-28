def positive_sum(arr):
    positive_total = 0
    for i in arr:
        if i > 0 and i != 0:
            positive_total += i
        
    return positive_total



print(positive_sum([1, -4, 7, 12]))