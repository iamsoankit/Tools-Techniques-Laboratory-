def armstrong_no(n):
    sum=0
    temp=n
    while temp>0:
        digit = temp % 10
        sum += digit **3
        temp //= 10
    return n==sum

print(armstrong_no(153))
    