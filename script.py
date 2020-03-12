############################################
#######     PROJECT EULER      #############
############################################

from itertools import permutations 
import math as m
from functools import reduce
import numpy as np
#test to check git#

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
        while i<=int(no/2):
            if no%i==0:
                l.append(i)
                no=no//i
            else:
                i+=1
    #print(l)
    l.append(no)
    return l 
    
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
        if isprime(i):
            fac_list.append(i)
        else:
            factors=prime_factorization(i)
            lis=fac_list[:]
            for i in factors:
                if i not in lis:
                    fac_list.append(i)
                else:
                    lis.remove(i)
        print(fac_list)
    print(reduce((lambda x, y: x * y), fac_list))

#########################
########    7  #########
########################    
def nth_prime(n):
    i=0;j=2;
    while i<n:
        if isprime(j):
            j+=1
            i+=1
        else:
            j+=1
    print(j-1)
    
#########################
########    8  #########
########################
def largestin_kdigits():
    f=open('tmp.txt', 'r')
    lines=f.readlines()
    lines=[x[:-1] for x in lines]
    s=''.join(lines)
    wind=13
    maxprod=0
    for i in range(len(s)-wind):
        if '0' in s[i:i+wind]:
            continue
        else:
            maxprod=max(maxprod,reduce((lambda x,y:int(x)*int(y)),s[i:i+wind]))
    print(maxprod)

#########################
########    9  #########
########################
def triplet():
    a=1;b=a+1;
    while b<1000 and a<1000:
        if a**2+b**2==(1000-a-b)**2:
            print(a,b)
            break
        else:
            if b==999:
                a+=1;b=a+1
            else:
                b+=1

#########################
########    11  #########
########################
def prod_grid(n):
    f=open('11.txt','r')
    arr=np.empty((20,20))
    lines=[x[:-1] for x in f.readlines()]
    for l in lines:
        l1=l.split(' ')
        arr[lines.index(l)]=np.asarray(l1)
    mx_prod=0
    #horz
    for i,j in [(x,y) for x in range(20) for  y in range(20-n)]:
        mx_prod=max(arr[i,j:j+n].prod(),mx_prod)
    #vert
    for i,j in [(x,y) for x in range(20-n) for  y in range(20)]:
        mx_prod=max(arr[i:i+n,j].prod(),mx_prod)
    #flip diag    
    flipped_arr=np.fliplr(arr)
    for i in range(-20+n,20-n):
        diag_arr=flipped_arr.diagonal(i)
        for j in range((20-abs(i))-n+1):
            diagonal_slice=diag_arr[j:j+n]            
            mx_prod=max(diagonal_slice.prod(),mx_prod)
    #diag
    for i in range(-20+n,20-n):
        diag_arr=arr.diagonal(i)
        for j in range((20-abs(i))-n+1):
            diagonal_slice=diag_arr[j:j+n]
            mx_prod=max(diagonal_slice.prod(),mx_prod)

    print(mx_prod)
    
#########################
########    12  #########
########################    
#no of factors = a+1 * b+1 * c+1 ... where a,b,c are powers of prime factors
def triangle_factos(n):
    i=0
    while(True):
        i+=1
        tri_sum=(i*(i+1))//2
        prime_facs=prime_factorization(tri_sum)
        unq_pf=set(prime_facs)
        powers=[prime_facs.count(i)+1 for i in unq_pf]
        if reduce((lambda x,y:x*y),powers)>n:
            break
    print(tri_sum)
                        
#########################
########    13  #########
######################## 
#solve it using big int also (to do)
def sumoofdigits():
    with open('12.txt','r') as file1:
        lines=file1.readlines()
    l=[]
    for i in lines:
        l.append(int(i))
    print(reduce((lambda x,y:x+y),l))
    
#########################
########    14  #########
########################
def collatz(n=1000000):
    dct={}
    i=2
    while(i<n):
        keys=dct.keys()
        j=i
        l=1
        #print(dct)
        while(j!=1):
            #print(j)
            if j in keys:
               l+=dct[j]
               dct[i]=l
               i+=1
               break
            else: 
                if j%2==0:
                    j=j//2
                elif j%2!=0:
                    j=3*j+1
                l+=1
            if j==1:
                dct[i]=l
                i+=1    
    print(max(dct,key=dct.get))    

#########################
########    15  #########
########################
grid_d=np.zeros((50,50))
def grid_paths(m=20,n=20):
    if m==1 or n==1:
        return 1
    else:
        if  grid_d[m-1][n]==0:
            grid_d[m-1][n]=grid_paths(m-1,n)
        if grid_d[m][n-1]==0:
            grid_d[m][n-1]=grid_paths(m,n-1)
        i=grid_d[m-1][n];j=grid_d[m][n-1]        
        return i+j

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
    print(f'No of circular primes under {n} : {c}')
    
