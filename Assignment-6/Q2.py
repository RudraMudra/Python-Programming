def checkAnagrams(str, str1):
      res_str = ' '.join(sorted(str))
      res_str1 = ' '.join(sorted(str1))
      if(res_str == res_str1):
            return True
      else:
            return False
print(checkAnagrams("kutla", "tulka"))
