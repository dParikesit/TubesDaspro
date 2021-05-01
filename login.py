from hash import hash

def login(users):
  username = input('Masukan username: ')
  password = hash(input('Masukan password: '))
  id = -1
  role = ''
  name = ''

  for user in users:
    if user[1]==username:
      id = user[0]
      name = user[2]
      if user[4]==password:
        role = user[5]

  while id == -1:
    print('User tidak ditemukan')
    username = input('Masukan username: ')
    password = hash(input('Masukan password: '))
    for user in users:
      if user[1]==username:
        id = user[0]
        name = user[2]
        if user[4]==password:
          role = user[5]
  
  while role =='':
    print('Password salah')
    password = hash(input('Masukan password: '))
    for user in users:
      if user[1]==username:
        if user[4]==password:
          role = user[5]
  
  return id, role, name

  