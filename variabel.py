# Bikin variabel buat storing data
from load import loader                                 #F14

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
  "name":''
}

loader(user, gadget, gadget_borrow, gadget_return,consumable, consumable_history, header_user, header_gadget,header_gadget_borrow, header_gadget_return, header_consumable,header_consumable_history)