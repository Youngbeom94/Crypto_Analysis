# -------------------------------
# 암호분석 2020.04.10, 20175204김영범
# -------------------------------

#------------------------------------------------------------------
def gcd_iteration(a,b):
    while b!=0:
        r = a%b
        # print('%d = (%d * %d) + %d' %(a,b,a//b,r))
        a , b = b , r
    return a

def xgcd_iteration(a,b):
    an, bn = a, b
    ua, va, ub, vb = 1, 0 ,0, 1 #an = ua * a + va *b , bn = ub *b + vb*b
    while bn != 0:
        # print('%d = %d*%d + %d*%d , %d = %d*%d + %d*%d ' %(an,ua,a,va,a,b,bn,ub,bn,vb))
        q = an//bn
        an , bn = bn , an - bn*q
        ua , va , ub, vb = ub ,vb , ua-ub*q, va-vb*q
    return an, ua, va # an is gcd , ua : x, va is x


def modInv(a,m):
    if gcd_iteration(a,m) != 1 :
        print("GCD_ERROR")
        return None
    an, mn = a, m
    ua, va, um, vm = 1, 0 ,0, 1 #an = ua * a + va *b , bn = ub *b + vb*b
    while mn != 0:
        # print('%d = %d*%d + %d*%d , %d = %d*%d + %d*%d ' %(an,ua,a,va,a,b,bn,ub,bn,vb))
        q = an//mn
        an , mn = mn , an - mn*q
        ua , va , um, vm = um ,vm , ua-um*q, va-vm*q
    return ua % m # an is gcd an = 1 = ua*a + va*m


#------------------------------------------------------------------


x = 63
y = 90
d,xn,yn = xgcd_iteration(x,y) 
# print('gcd (%d, %d) = %d' %(x,y,gcd_iteration(x,y)))
# print('gcd(%d, %d) = %d = (%d) *%d + (%d) *%d' %(x,y,d,xn,x,yn,y))
# print(modInv(2,5))