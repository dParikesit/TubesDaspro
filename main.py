from login import login

# Bikin variabel buat storing data
choice = ''
user=[]
gadget=[]
gadget_borrow = []
gadget_return = []
consumable = []
consumable_history = []
user_now = {
  "id":'',
  "role":'',
}

def is_integer(n):
  try:
    int(n)
    return True
  except ValueError:
    return False

def is_float(n):
  try:
    float(n)
    return True
  except ValueError:
    return False

def isAdmin(role):
  if role=='Admin':
    return True
  else:
    return False

def load_user(datas, path):
  f = open(path, 'r')
  raw_lines = f.readlines()
  f.close()
  post_load_data(datas, raw_lines)

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
    
    # Typecasting yang bisa jadi int atau float
    for i in range(len(arr)):
      if is_integer(arr[i]):
        arr[i]=int(arr[i])
      elif is_float(arr[i]):
        arr[i]=float(arr[i])
    
    # Memasukkan ke variabel
    datas.append(arr)

def pre_save_data(datas):
  data_string = ''
  for data in datas:
    data = [str(item) for item in data]
    data = ';'.join(data) + '\n'
    data_string += data
  return data_string

def save_data(pre_datas, path):
  f = open(path, 'w')
  f.write(pre_datas)
  f.close()

# Save Data
''' save_data(pre_save_data(consumables), './file_csv/consumable.csv') '''

load_user(user, './file_csv/user.csv')
user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))

while (user_now['id'] == ''):
  user_now['id'], user_now['role'] = login(user, input('Masukan username: '), input('Masukan password: '))

print(user_now['role'])
