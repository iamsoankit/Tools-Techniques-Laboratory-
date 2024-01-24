def find_greatest(a,b,c):
    if (a >= b) and (a >= c):
        greatest=a
    elif (b >=a ) and (b >= c):
        greatest=b
    else:
        greatest=c
    return greatest

print(find_greatest(46,32,54))

    
    