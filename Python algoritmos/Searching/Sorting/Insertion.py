def insertion(array):
    for i in range(1,len(array)):
        chave =  array[i]
        j=i-1
        while j>=0 and chave < array[j]:
            array[j+1]=array[j]
            j=j-1
            array[j+1]=chave
array=[0,1,2,3]
insertion(array)
print(array)