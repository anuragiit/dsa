def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            print(p,end=' ')
 
if __name__=='__main__':
    n = int(input())
    print ("Following are the prime numbers smaller")
    print("than or equal to", n)
    SieveOfEratosthenes(n)
