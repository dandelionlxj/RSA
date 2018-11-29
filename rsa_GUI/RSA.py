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


def gcd(x,y): 
    '''
    求最大公因子
    '''
    if (y>x):
        x,y=y,x
    while(y!=0):
        x,y=y,x%y
    return x


def choice_prime(keylength):
    """
    随机选出素数
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
    print('p:'+str(p))
    print("q:"+str(q))
    print('n:'+str(n))
    f=(p-1)*(q-1)
    print('φ(n):'+str(f))
    while True:
        e=random.randint(1,f) 
        if gcd(e,f)==1:
            break
    print('e:'+str(e))
    d=ext_gcd(e,f)
    print('d:'+str(d))
    return (n,e,d)


def ext_gcd(e, m):
    """
    扩展欧基里德算法
    """
    if gcd(e,m)!=1:
        return None
    u1,u2,u3 = 1,0,e
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m


def encrypt(m,e,n):
    '''
    加密
    '''
    return fast_mod(m,e,n)


def decrypt(c,d,n):
    '''
    解密
    '''
    return fast_mod(c,d,n)


if __name__== '__main__':
    (n,e,d)=key(60)
    #从0到2的20次方随机选取一个数字作为明文
    m=random.randint(0,1<<20) 
    print('M:'+str(m))
    C=encrypt(m,e,n)
    M=decrypt(C,d,n)
    print('encrypt result:'+str(C))
    print('decrypt result:'+str(M))
    

