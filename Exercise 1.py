
# coding: utf-8

# In[25]:


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
res = prime_factors(45)

print("prime factors res:", res)

#Claude is the code taking input in the comand line? Thx to Miguel for explaining some stuff


# In[21]:




