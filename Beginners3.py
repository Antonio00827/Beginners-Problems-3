a = input("You come across a lake. Do you want to swim or wait for a boat?")
if a == "swim":
  print("You get eaten by a shark. GAME OVER")
  break
elif a == "wait":
  b = input("You come to a cave. Do you want to venture in or walk on?")
  if b == "venture":
    print("You are squished by boulders and never seen again. GAME OVER")
    break
  elif b == "walk":
    c = input("You’re at a crossroads. Do you go left, right, or straight?")
    if c == "left":
      print("You are trampled by a herd of wildebeest. GAME OVER")
      break
    elif c == "straight":
      print("You get stung by a poisonous wasp. GAME OVER")
      break
    elif c == "right":
      print("You found TREASURE. YIPPEEEEEEEE")
      break
