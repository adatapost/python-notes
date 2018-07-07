def get_primes(start_value, stop_value):
    prime_no = []
    for a in range(start_value,stop_value+1):
        b = 1
        c = 2
        while c<=a/2:
            if a % c ==0:
                b += 1
            c += 1
        if b == 1:
            prime_no.append(a)
    return prime_no

r1 = get_primes(10,50)   
r2 = get_primes(1,20)

print(r1)
print(r2)

 
