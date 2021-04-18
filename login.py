from hash import hash

def login(users, username, password):
  hashed = hash(password)
  id = -1
  role = ''

  for user in users:
    if user[1]==username:
      id = user[1]
      if user[4]==hashed:
        role = user[5]
  
  if id == -1:
    print('User tidak ditemukan')
  elif role == '':
    print('Password salah')
  
  return id, role

  