def mult():
    sum=0
    for i in range(3, 1000, 3):
        sum+=i
    for i in range(5, 1000, 5):
        sum+=i
    for i in range(15, 1000, 15):
        sum-=i
    return sum
print(mult())
