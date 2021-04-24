from datetime import datetime
from helper import is_integer, is_float, is_datetime

def load_data(datas, header_datas, path):
  f = open(path, 'r')
  raw_lines = f.readlines()
  f.close()
  post_load_data(datas, raw_lines)
  
  # Memisahkan data dengan header nya
  for head in datas[0]:
    header_datas.append(head)
  datas.pop(0)

def post_load_data(datas, raw_lines):
  lines = [raw_line.replace("\n", "").replace("\ufeff","") for raw_line in raw_lines]
  for line in lines:
    # Cek ada berapa kolom pada csv
    panjang=1
    for i in range(len(line)):
      if line[i] == ';':
        panjang += 1
    
    # Mengubah string jadi array data
    koma = -1
    point=0
    arr = ['' for i in range(panjang)]
    for i in range(len(line)):
      if line[i]==';':
        arr[point]=line[koma+1 : i]
        koma=i
        point+=1
      elif i==(len(line)-1):
        arr[point]=line[koma+1 : i+1]
    
    # Typecasting yang bisa jadi int atau float atau datetime
    for i in range(len(arr)):
      if is_integer(arr[i]):
        arr[i]=int(arr[i])
      elif is_float(arr[i]):
        arr[i]=float(arr[i])
      elif is_datetime(arr[i]):
        arr[i]=datetime.strptime(arr[i], '%d/%m/%Y')
    
    # Memasukkan ke variabel
    datas.append(arr)

def batch_load(user, gadget, gadget_borrow, gadget_return, consumable, consumable_history, header_user, header_gadget, header_gadget_borrow, header_gadget_return, header_consumable, header_consumable_history):
  load_data(user, header_user, './file_csv/user.csv')
  load_data(gadget, header_gadget, './file_csv/gadget.csv')
  load_data(gadget_borrow, header_gadget_borrow, './file_csv/gadget_borrow_history.csv')
  load_data(gadget_return, header_gadget_return, './file_csv/gadget_return_history.csv')
  load_data(consumable, header_consumable, './file_csv/consumable.csv')
  load_data(consumable_history, header_consumable_history, './file_csv/consumable_history.csv')