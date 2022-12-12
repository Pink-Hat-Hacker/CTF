from Crypto.Util.number import inverse

e = 3
n = 245841236512478852752909734912575581815967630033049838269083
c = 74090092363278558232634733865409254973829605823913391587517

p = 416064700201658306196320137931
q = 590872612825179551336102196593

phi = (p - 1) * (q - 1)
print(phi)

# d = inverse of e % phi
d = inverse(e, phi)
print(d)

# m = c ^ d % n
m = pow(c, d, n)
print(hex(m))

'''
make an RSA ctf problem
m = PINKY{pH!_i$_th3_kEy} =


'''