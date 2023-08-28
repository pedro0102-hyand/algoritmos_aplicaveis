def selection(array):
    n=len(array)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if array[j]<array[min]:
                min=j
                array[i],array[min]=array[min],array[i]
array=[1,5,7,18,90]
selection(array)
print(array)