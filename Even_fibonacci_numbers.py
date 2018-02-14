def even_fibonacci_numbers():
    sum=0
    i=1
    k=1
    while True:
        i+=k
        if i > 4000000:
            return sum
        if i//2==i/2: sum+=i
        k+=i
        if k>4000000:
            return sum
        if k//2==k/2: sum+=k
print(even_fibonacci_numbers())
