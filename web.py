'''
[webhacking.kr]
------------
# Given:
------------
ID : guest
PW : 123qwe
'''
import base64
import urllib.parse

user = b"admin"
password = b"nimda"

for i in range(20):
    user = base64.b64encode(user)
    password = base64.b64encode(password)

encypted_u = user.decode('utf-8')
encypted_p = password.decode('utf-8')

encypted_u = encypted_u.replace('1', '!').replace('2', '@').replace('3', '$').replace('4', '^').replace('5', '&').replace('6','*').replace('7', '(').replace('8',')')
encypted_p = encypted_p.replace('1', '!').replace('2', '@').replace('3', '$').replace('4', '^').replace('5', '&').replace('6','*').replace('7', '(').replace('8',')')

encypted_u = urllib.parse.quote(encypted_u)
encypted_p = urllib.parse.quote(password)

#idk what they are printing ok
print("\033[1;31;40m user id: \033[0m")
print(encypted_u)
print("\033[1;36;40m user password: \033[0m")
print(encypted_p)