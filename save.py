def pre_save_data(datas):
  data_string = ''
  for data in datas:
    data = [str(item) for item in data]
    data = ';'.join(data) + '\n'
    data_string += data
  return data_string

def save_data(datas, path):
  f = open(path, 'w')
  f.write(pre_save_data(datas))
  f.close()

def batch_save(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history):
  save_data(user, './file_csv/user.csv')
  save_data(gadget, './file_csv/gadget.csv')
  save_data(gadget_borrow, './file_csv/gadget_borrow_history.csv')
  save_data(gadget_return, './file_csv/gadget_return_history.csv')
  save_data(consumable, './file_csv/consumable.csv')
  save_data(consumable_history, './file_csv/consumable_history.csv')