def func_str():
  """ функция перевода из нижнего резистра
  в верхний регистр всех букв """

  a = str(input("Введите строку"))
  x = a.upper()
  return (x)

def func_strup():
  """ функция перевода из нижнего резистра
  в верхний регистр только первых букв"""
  a = str(input("Введите строку"))
  x = a.title()
  return (x)

print (func_str())
print (func_strup())

