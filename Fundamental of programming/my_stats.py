def my_mean(L):
    total = sum(L)
    return total / len(L)

def my_variance(L):
    mean = my_mean(L)
    squared_diff = [(x - mean) ** 2 for x in L]
    return my_mean(squared_diff)

def my_mode(L):
    frequency = {}
    for num in L:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    return max(modes)
