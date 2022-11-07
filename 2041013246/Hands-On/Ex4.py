a,b,c,d,e,f = [float(i) for i in input("Enter a,b,c,d,e,f : ").split(',')]
diff = a*d-b*c
if diff != 0:
      x=(e*d-b*f)/diff
      y=(a*f-e*c)/diff
      print(f"x is {x} and y is {y}")
else:
      print("The equation has no solution")
