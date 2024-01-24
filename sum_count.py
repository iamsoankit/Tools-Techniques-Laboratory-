def sum_count(n):
    sum = 0
    count = 0
    while n > 0:
        digit = n % 10
        sum += digit
        count += 1
        n //= 10
    return sum, count

print(sum_count(123)) 