def total_average(list):
    if len(list)>1:
        return (sum(list), sum(list)/len(list))
    return (0, None)

print(total_average([2,4,6]))