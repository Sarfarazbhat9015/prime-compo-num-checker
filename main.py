def prime (m,n):
    primes=[]
    compo=[]
    c=0
    d=0
    if m==1:
        m+=1
    for i in range (m, n+1):
        for j in range (2, i):
            if i%j == 0:
                compo. append(i)
                c+=1
                break
        else:
            d+=1 
            primes.append(i)
    print( "Primes numbers in the range:")
    print (primes)
    print("Composites numbers in the range:")
    print (compo)
    print ("Count:",d, "prime and",c, "composite numbers in the range.") 

m=int(input("First limit:"))
n=int(input("Last limit."))
prime(m,n)