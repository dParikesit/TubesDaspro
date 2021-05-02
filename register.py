from hash import hash
from helper import is_Admin

def register(user, user_now):
  if is_Admin(user_now)==False:
    print('Anda tidak dapat membuat user')
  else:
    id = len(user)+1
    nama = input('Masukan nama: ')
    username = input('Masukan username: ')
    is_exist = False
    
    for each in user:
      if username == each[1]:
        is_exist = True
    
    while is_exist==True:
      print('Username telah ada. Masukkan yang berbeda')
      username = input('Masukan username: ')
      for each in user:
        if username == each[1]:
          is_exist = True

    password = hash(input('Masukan password: '))
    alamat = input('Masukan alamat: ')
    role = 'User'

    new_user = [id,username,nama,alamat,password,role]
    user.append(new_user)
    print('User',username,'telah berhasil register ke dalam Kantong Ajaib')
  