from hash import hash

def register():
  nama = input('Masukan nama: ')
  username = input('Masukan username: ')
  password = hash(input('Masukan password: '))
  alamat = input('Masukan alamat: ')

  return nama,username,password,alamat

print(register())