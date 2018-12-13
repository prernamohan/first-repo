def find_hypotenuse(x,y):
  import math
  if x > 0 and y > 0:
    z = x * x + y * y
    hypotenuse = math.sqrt(z)
    print(f"The hypotenuse of the right triangle with sides {x} and {y} is {hypotenuse}")
  else:
    print(f"This shape is not a right triangle")

find_hypotenuse(3,4)