from hash import hash

def login(users, username, password):
  hashed = hash(password)
  id = ''
  role=''
  for user in users:
    if user[4]==hashed:
      id = user[0]
      role = user[5]
      break
  
  return id, role