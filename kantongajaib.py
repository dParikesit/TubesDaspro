from register import register
from login import login
from load import batch_load, parser, path_loader
from exit import exit
from helper import is_Admin

# Bikin variabel buat storing data
choice = ''
user=[]
gadget=[]
gadget_borrow = []
gadget_return = []
consumable = []
consumable_history = []
header_user = []
header_gadget = []
header_gadget_borrow = []
header_gadget_return = []
header_consumable = []
header_consumable_history = []
user_now = {
  "id":-1,
  "role":'',
}

path_link = parser()
if (path_loader(path_link) == True):
  batch_load(path_link, user, gadget, gadget_borrow, gadget_return,consumable, consumable_history, header_user, header_gadget,header_gadget_borrow, header_gadget_return, header_consumable,header_consumable_history)
  print('Selamat datang di "Kantong Ajaib" !')
else:
  print('Tidak ada nama folder yang diberikan')
  print('Usage: python kantongajaib.py <nama_folder>')

user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))
while (user_now['id'] == -1 or user_now['role'] == ''):
  user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))

print('Halo', user_now['id'])

choice = input('>>> ')
while choice != 'exit':
  if choice == 'register':
    if is_Admin(user_now['role']):
      print('Anda tidak dapat membuat user')
      choice = input('>>> ')
    else:
      nama,username,password,alamat = register()
      id = (len(user))
      role = 'User'
      user.append([id, username, nama, alamat, password, role])
      print('User telah ditambah')
      choice = input('>>> ')
  else:
    choice = input('>>> ')


exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)
