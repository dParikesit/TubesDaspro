from datetime import datetime
from os import path, mkdir

def pre_save_data(datas):
  data_string = ''
  for data in datas:
    for i in range(len(data)):
      if isinstance(data[i], datetime):
        data[i] = data[i].strftime('%d/%m/%Y')
    data = [str(item) for item in data]
    data = ';'.join(data) + '\n'
    data_string += data
  return data_string

def save_data(datas, header_datas, file_path):
  datas.insert(0, header_datas)
  f = open(file_path, 'w')
  f.write(pre_save_data(datas))
  f.close()
    
  

def save(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history):
  folder = (input('Masukkan nama folder penyimpanan: ')) 
  path_link = './'+ folder

  if path.isdir(path_link)==False:
    mkdir(path_link)

  print("Saving...")
  print("Data telah disimpan pada ", folder, "!")
  
  save_data(user, header_user, path_link+'/user.csv')
  save_data(gadget, header_gadget, path_link+'/gadget.csv')
  save_data(gadget_borrow, header_gadget_borrow, path_link+'/gadget_borrow_history.csv')
  save_data(gadget_return, header_gadget_return, path_link+'/gadget_return_history.csv')
  save_data(consumable, header_consumable, path_link+'/consumable.csv')
  save_data(consumable_history, header_consumable_history, path_link+'/consumable_history.csv')

  