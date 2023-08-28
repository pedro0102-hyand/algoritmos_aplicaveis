def heap(array,n,i):
    maior=i
    direita=2*i+2
    esquerda=2*i+1
    if esquerda<n and array[esquerda]>array[maior]:
        maior=esquerda
    if direita < n and array[direita]>array[maior]:
        maior=direita
    if maior != i :
        array[i],array[maior] =  array[maior],array[i]
        heap(array,n,maior)
def heap(array):
    n=len(array)
    for i in range(n//2-1,-1,-1):
        heap(array,n,i)
    for i in range(n-1,0,-1):
        array[i],array[0]=array[0],array[i]
        heap(array,i,0)
array=[9,2,3,4,7]
heap(array)
print(array)
    