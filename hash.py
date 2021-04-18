def hash(password):
  hashed = ''
  # Hashing bekerja dengan mengubah tiap char jadi ascii kemudian di concat
  for i in range(len(password)):
    hashed += str(ord(password[i])+10)
  return hashed