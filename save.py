def pre_save_data(datas):
  data_string = ''
  for data in datas:
    data = [str(item) for item in data]
    data = ';'.join(data) + '\n'
    data_string += data
  return data_string

def save_data(datas, header_datas, path):
  datas.insert(0, header_datas)
  f = open(path, 'w')
  f.write(pre_save_data(datas))
  f.close()

def batch_save(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history):
  save_data(user, header_user, './file_csv/user.csv')
  save_data(gadget, header_gadget, './file_csv/gadget.csv')
  save_data(gadget_borrow, header_gadget_borrow, './file_csv/gadget_borrow_history.csv')
  save_data(gadget_return, header_gadget_return, './file_csv/gadget_return_history.csv')
  save_data(consumable, header_consumable, './file_csv/consumable.csv')
  save_data(consumable_history, header_consumable_history, './file_csv/consumable_history.csv')

