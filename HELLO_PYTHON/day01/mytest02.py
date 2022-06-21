#100에서 200사이의 짝수의 합

arr = range(100, 200+1)

sum = 0

for i in arr:
    if i%2 == 0:
        sum += i 
    
print("sum", sum)


