def replacewithstar(str):
      stars = ' '
      for i in range(0, len(str)):
            if(str[i] == str[i-1]):
               stars = stars[:i+1] + '*'
            else:
                  stars += str[i]
      return stars
print(replacewithstar('balloon'))
