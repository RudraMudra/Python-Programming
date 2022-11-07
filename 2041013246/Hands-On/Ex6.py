x,y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))

if x>0 and y>0:
      print("point (",x,",",y, ") lies in 1st quadrant")

elif x<0 and y>0:
      print("point (",x,",",y, ") lies in 2nd quadrant")
elif x<0 and y<0:
      print("point (",x,",",y, ") lies in 3rd quadrant")
elif x>0 and y<0:
      print("point (",x,",",y, ") lies in 4th quadrant")


elif x==0 and y==0:
      print("point (",x,",",y, ") lies at the origin. ")

elif y==0 and x != 0:
      print("point (",x,",",y, ") lies on x-axis")

elif x==0 and y != 0:
      print("point (",x,",",y, ") lies on y-axis")
