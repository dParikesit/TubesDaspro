def hash(password):
  hashed = ''
  final = ''
  # Hashing bekerja dengan mengubah tiap char jadi ascii yang ditambah 10 kemudian diconcat. Hasil concat ini kemudian diambil tiap 3 karakter (terduplikat) untuk dikembalikan jadi string character.
  for i in range(len(password)):
    hashed += str(ord(password[i])+10)
  
  for i in range(len(hashed)-3):
    hash3 = int(hashed[i]+hashed[i+1]+hashed[i+2])
    if hash3>126:
      hash3 -= 33
    elif hash3<33:
      hash3 += 33
    final += chr(hash3)
  
  return str(final)