# -*- coding = utf-8 -*-
import math
import random
def fast_mod(x,n,m):
    '''
    快速模指运算
    '''
    a=1
    b=x
    while True:
        temp=n
        if(n%2==1):
            a=a*b%m
        b=b*b%m
        n=n//2
        #print(a)
        if temp<1:
            return a

def isPrime(n):
    """
    判断一个数是否为素数
    :param type(n) == int
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def gcd(x,y): 
    '''
    求最大公因子
    '''
    if (y>x):
        x,y=y,x
    while(y!=0):
        x,y=y,x%y
    return x

def Phi(n) :
    """
    计算欧拉函数
    """
    if(n<=0):
        print('请输入正数')
    elif(n==1):
        return 1
    elif(isPrime(n)):
        return(n-1)
    else:
        p=1
        for i in range(2,n):
            if(gcd(i,n)==1):
                p+=1
        return p

def test(n):
    j=n-1
    m=0
    for i in range(1,n-1):
        if ((n-1)%j==0 and j%2==1):
           m=j
        else:
            j=j-1
    a=(n-1)/m
    t=0
    while(2**t!=a):
        t+=1
    return m,t
           
def choice_prime(keylength):
    """
    随机选出素数p,q
    """
    while True:
        #选择随机数
        n = random.randint(0, 1<<keylength)
        if n % 2 != 0:
            found = True
            #随机性测试
            for i in range(0, 10):
                if prime_test(n) == 'composite':
                    found = False
                    break
            if found == True:
                return n

def prime_test(n):
    """
    测试n是否为素数
    """
    q = n - 1
    k = 0
    #寻找k,q 是否满足2^k*q =n - 1 
    while q % 2 == 0:
        k += 1
        q = q // 2
    a = random.randint(2, n-2)
    #如果 a^q mod n= 1, n 可能是一个素数
    if fast_mod(a, q, n) == 1:
        return "inconclusive"
    #如果存在j满足 a ^ ((2 ^ j) * q) mod n == n-1, n 可能是一个素数
    for j in range(0, k):
        if fast_mod(a, (2**j)*q, n) == n - 1:
            return "inconclusive"
    #n 不是素数
    return "composite"

def key(key_len):
    '''
    求n,e,d
    '''
    p=choice_prime(key_len)
    q=choice_prime(key_len)
    n=q*p
    f=(p-1)*(q-1)
    while true:
        f1=random.randint(1,f)
        if gcd(f1,f)==1:
            e=f1
            break

def ext_gcd(a, b):
    """
    扩展欧几里得算法
    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_gcd(b, a % b) 
        x, y = y, (x - (a // b) * y)
        return x, y, q
    