def binario(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        mid_value=array[mid]
        if mid_value==target:
            return mid
        elif mid_value<target:
            left=mid+1
        else:
            right=mid-1
    return -1
array=[0,1,3,4,5,6,7,8]
target=9
resultado=binario(array,target)
if resultado !=-1:
    print(f"foi encontrado no {resultado}")
else:
    print(f"nao esta no array")