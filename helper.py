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

def is_Admin(role):
  if role=='Admin':
    return True
  else:
    return False