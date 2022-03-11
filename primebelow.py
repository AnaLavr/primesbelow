def is_prime(num):
    b=0
    for i in range(2,num):  
        if num%i == 0:
            b += 1
    if b!=0:
        return('False')    
    else:
        return('True')
    


def primes_below(n):
    l=[]
    for i in range(2,n):
        if is_prime(i)=='True':
            l.append(i)
    return(l)

print(primes_below(17))