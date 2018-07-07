def is_prime(no):
    """
    This function returns true if given parameter is prime, returns
    false otherwise
    """
    for a in range(2, no // 2 +1 ):
        if no % a == 0:
            return False
    return True 

# Call the function 
print(is_prime(33)) 

if is_prime(10):
    print("It is prime")
else:
    print("Not prime")

# Print all primes between 1 to 100
for a in range(1,11):
    if is_prime(a): print(a)

    
