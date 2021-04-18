# Bikin variabel buat storing data
consumables = []
gadget_borrow = []
gadget_return = []
gadget = []
users=[]
user_now = {
  "name":'',
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

# Load data
load_user(users, './file_csv/user.csv')

# Akses Data


# Save Data
''' save_data(pre_save_data(consumables), './file_csv/consumable.csv') '''


