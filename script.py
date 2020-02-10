############################################
#######     PROJECT EULER      #############
############################################

from itertools import permutations 
import math as m


###########################################
#checks prime
def isprime(n):
    if n==2 or n==3:
        return True    
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True

#gives list of all rotations of give sequence list
def circular_rotation(digits):
    perm=[]
    l=len(digits)
    digits=digits+digits
    for i in range(l):
        perm.append(digits[i:i+l])
    return perm

# gives fibonacci sequence to certain value
def fibo_seq(to_value,a=0,b=1):
    l=[a]
    while b<to_value:
        l.append(b)
        b+=a
        a=l[-1]
    return l    
    
def palindrome(s):
    l=len(s)
    if l%2==0:
        if s[:(l//2)]==s[(l//2):][::-1]:
            return True
    elif s[:int(l/2)]==s[int(l/2)+1:][::-1]:
        return True
    return False
   
def prime_factorization(n):
    l=[]
    no=n;i=2
    if isprime(n):
        l.append(no)
    else:
        while i<=int(n/2):
            if no%i==0:
                l.append(i)
                no=no//i
            else:
                i+=1
    print(l)
###########################################

#########################
########    1  #########
########################    
def sum_multiples(n): # of 3 or 5
    l3=[i*3 for i in range(n) if i*3<n ]
    l5=[i*5 for i in range(n) if i*5<n]
    l=list(set(l3+l5))
    print(l)
    print(sum(l,0))
    
    
#########################
########    2  #########
########################
def sum_even_fib(to_value):
    l=fibo_seq(to_value,1,2)
    s=0
    for no in l:
        if no%2==0:
            s+=no
    return s
    
#########################
########    3  #########
########################
def largest_prime_factor(n):
    if isprime(n):
        print(n)
    for i in range(int(m.sqrt(n)),1,-1):
        if n%i==0:
            if isprime(i):
                print(i)
                break; 
                
#########################
########    4  #########
########################
def palindromic(digits=3):
    maxm=int(''.join(['9' for i in range(digits)]))
    minm=(maxm+1)//10
    a=maxm;b=maxm
    l=set()
    while a>minm:
        if palindrome(str(a*b)):
            #print(a,b)
            l.add(a*b)
            if b==minm:
                a-=1
                b=maxm
            else:
                b-=1
        else:
            if b==minm:
                a-=1
                b=maxm
            else:
                b-=1
    print(max(l))
    
#########################
########    5  #########
########################
def evenly_divisible(to_value):
    fac_list=[]
    for i in range(2,to_value+1):
        continue
#########################
########    35  #########
########################    
def circular_primes(n):
    c=0
    for i in range(2,n):
        if isprime(i):
            digits=[]
            #print(i)    
            for j in range(len(str(i))):
                digits.append(str(i)[j])
            #print(digits)
            perm = circular_rotation(digits)
            flg=1
            for no in perm:
                no = int(''.join(list(no)))
                if not isprime(no):
                    flg=0
                    break               
            if flg==1:
                c+=1
                print(no)
    print(f'NO of circular primes under {n} : {c}')
