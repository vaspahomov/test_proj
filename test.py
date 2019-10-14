import itertools
import hashlib

for e in range(1000000, 10000000):
    password = str(e).ljust(8, '0')
    if hashlib.sha1(password.encode()).hexdigest() == '6ddc3c39fbe045ad9712232e48c4c9a6c4053a0a':
        print('OH SHIT ')
        print(password)

for e in range(10000000, 100000000):
    password = str(e)
    if hashlib.sha1(password.encode()).hexdigest() == '6ddc3c39fbe045ad9712232e48c4c9a6c4053a0a':
        print('OH SHIT ')
        print(password)
