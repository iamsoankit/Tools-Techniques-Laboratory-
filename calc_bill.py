def calc_bill(units):
    if units <= 100:
        bill =units*2.5
    elif units <=100:
        bill= 100*2.5 + (units-100)*4
    else:
        bill=100*2.5 + 100*4 + (units-200)*5
    
    return bill

print (calc_bill(250))


