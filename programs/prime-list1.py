def get_primes_imp(no1, no2):
    result = []
    for a in range(no1, no2+1):
        for b in range(2, (a+1) // 2):
            if a % b == 0:
                break
        else:
            result.append(a)
    return result

def get_primes(no1,no2):
    result = []
    for a in range(no1,no2+1):
        is_prime = 111
        for b in range(2,a):
            if a % b == 0:
                is_prime = 0
                break
        if is_prime:
            result.append( a )
    return result

# Call

a = get_primes(1,200)            
b = get_primes(5000,5500)
print(a)
print(b)
          
                

                
                

 
            







