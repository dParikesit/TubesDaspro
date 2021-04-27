import sys

from register import register
from login import login
from load import batch_load, parser, path_loader
from helper import is_Admin
from MeminjamGadget import pinjam                       #F08
from MengembalikanGadget import kembalikan              #F09
from MemintaConsumable import minta                     #F10
from help import help                                   #F16
from exit import exit                                   #F17



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

def pilihan_program(choice) :
  if choice == 'register' :
      register()
  elif choice == 'login' :
      login()
#  elif choice == 'carirarity' :
#  elif choice == 'caritahun' :
#  elif choice == 'tambahitem' :
#  elif choice == 'hapusitem' :
#  elif choice == 'ubahjumlah' :
  elif choice == 'pinjam' :
      pinjam(user_now)
  elif choice == 'kembalikan' :
      kembalikan(user_now)
  elif choice == 'minta' :
      minta(user_now)
# elif choice == 'riwayatpinjam' :
# elif choice == 'riwayatkembali' :
# elif choice == 'riwayatambil' :
  elif choice == 'help' :
    help()
  else :
    print("Pilihan tidak ada dalam sistem kantongajaib")

path_link = parser()
if (path_loader(path_link) == True):
  batch_load(path_link, user, gadget, gadget_borrow, gadget_return,consumable, consumable_history, header_user, header_gadget,header_gadget_borrow, header_gadget_return, header_consumable,header_consumable_history)
  print('===== Selamat datang di "Kantong Ajaib" ! =====')
else:
  print('Tidak ada nama folder yang diberikan')
  print('Usage: python kantongajaib.py <nama_folder>')
  sys.exit()


user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))
while (user_now['id'] == -1 or user_now['role'] == ''):
  user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))

print('Halo!', user_now['id'])

choice = input('>>> ')
pilihan_program(choice)
while choice != 'exit':
  if choice == 'register':
    if is_Admin(user_now):
      print('Anda tidak dapat membuat user')
      choice = input('>>> ')
      pilihan_program(choice)
    else:
      nama,username,password,alamat = register()
      id = (len(user))
      role = 'User'
      user.append([id, username, nama, alamat, password, role])
      print('User telah ditambah')
      choice = input('>>> ')
      pilihan_program(choice)
  else:
    choice = input('>>> ')
    pilihan_program(choice)


exit(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history)