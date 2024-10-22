# https://asecuritysite.com/encryption/c_c
e=7923
d=10
N=3337
r=3
M=10
import libnum

cipher=M**e % N
print ('==Initial values ====')
print ('e=',e,'d=',d,'N=',N)
print ('message=',M,'r=',r)
print ('\n=============')

print ('\nInitial cipher:\t',cipher)

cipher_dash = (cipher * pow(r,e , N)) % N
print ('Eve gets Bob to decipher:\t',cipher_dash)


decipher = pow(cipher_dash,d , N)

print ('Bob says that the result is wrong:',decipher)

res = (decipher * libnum.invmod(r,N)) % N

print ('Eve determines as:',res)

if (res==M):
	print ('Eve has cracked message, as result is same as message')
else:
	print ('Eve has not cracked the message')