a = input('Enter a character : ')
if 65 <= ord(a)<=90:
    print('Upper Case')
elif 97<=ord(a)<=122:
      print('Lower Case')
elif 48<=ord(a)<=57:
      print('digit')
else:
      print('Special Character')
