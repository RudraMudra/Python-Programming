a = float(input("Enter the 1st number : "))
b = float(input("Enter the 2nd number : "))
      
i = 1
while(i <= a and i <= b):
      if(a % i == 0 and b % i == 0):
            val = i
      i = i+1
      
print("GCD of {0} and {1} = {2}".format(a,b,val))
