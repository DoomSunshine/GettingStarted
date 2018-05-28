def prime_factors(n):
    i = 2
    temp = []
    while i <= n: 
        if n % i == 0:
            print("i = ", i)
            print(i, " is divisor of ",n)
            print("----")
            
            temp.append(i)
            
            n = n / i
        else:
            i += 1
    return temp

number = int(input("Choose a number"))

res = prime_factors(number)

print("prime factors res:", res)
