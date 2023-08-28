def counting(x):
    maximo=max(x)
    minimo=min(x)
    range=maximo-minimo+1
    counting=[0]*range
    for n in x:
        counting[n-minimo]+=1
    sorted =0
    for i in range(range):
        while counting[i]>0:
            x[sorted]=i+minimo
            sorted=sorted+1
            counting[i]=counting[i]-1