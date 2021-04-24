from register import register
from login import login
from load import batch_load
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

# Save Data
''' save_data(pre_save_data(consumables), './file_csv/consumable.csv') '''

batch_load(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)

user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))
while (user_now['id'] == -1 or user_now['role'] == ''):
  user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))

print('Halo', user_now['id'])

choice = input('Masukan pilihan: ')
while choice != 'exit':
  if choice == 'register':
    if is_Admin(user_now['role']):
      print('Anda tidak dapat membuat user')
      choice = input('Masukan pilihan: ')
    else:
      nama,username,password,alamat = register()
      id = (len(user))
      role = 'User'
      user.append([id, username, nama, alamat, password, role])
      print('User telah ditambah')
      choice = input('Masukan pilihan: ')
  else:
    choice = input('Masukan pilihan: ')


exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history)
