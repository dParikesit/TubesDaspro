from datetime import datetime

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

def is_Admin(user_now):
  if user_now['role'] =='Admin':
    return True
  else:
    return False

def is_datetime(date):
  try:
    datetime.strptime(date, '%d/%m/%Y')
    return True
  except ValueError:
    return False
    
