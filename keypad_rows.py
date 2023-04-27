def row1():
  global code
  R1.off()
  R2.on()
  R3.on()
  R4.on()
  
  if C1.is_pressed:
    print("1")
    code += "1"
    while C1.is_pressed:
      if C1.is_pressed == False:
        break
    
  elif C2.is_pressed:
    print("2")
    code += "2"
    while C2.is_pressed:
      if C2.is_pressed == False:
        break
  
  elif C3.is_pressed:
    print("3")
    code += "3"
    while C3.is_pressed:
      if C3.is_pressed == False:
        break
    
def row2():
  global code
  R1.on()
  R2.off()
  R3.on()
  R4.on()
  
  if C1.is_pressed:
    print("4")
    code += "4"
    while C1.is_pressed:
      if C1.is_pressed == False:
        break
  
  elif C2.is_pressed:
    print("5")
    code += "5"
    while C2.is_pressed:
      if C2.is_pressed == False:
        break
  
  elif C3.is_pressed:
    print("6")
    code += "6"
    while C3.is_pressed:
      if C3.is_pressed == False:
        break
    
def row3():
  global code
  R1.on()
  R2.on()
  R3.off()
  R4.on()
  
  if C1.is_pressed:
    print("7")
    code += "7"
    while C1.is_pressed:
      if C1.is_pressed == False:
        break
    
  elif C2.is_pressed:
    print("8")
    code += "8"
    while C2.is_pressed:
      if C2.is_pressed == False:
        break
    
  elif C3.is_pressed:
    print("9")
    code += "9"
    while C3.is_pressed:
      if C3.is_pressed == False:
        break
    
def row4():
  global code
  R1.on()
  R2.on()
  R3.on()
  R4.off()
  
  if C1.is_pressed:
    if active == True:
      print("*")
      code += "*"
      while C1.is_pressed:
        if C1.is_pressed == False:
          break
      
  elif C2.is_pressed:
    print("0")
    code += "0"
    while C2.is_pressed:
      if C2.is_pressed == False:
        break
    
  elif C3.is_pressed:
    print("#")
    code += "#"
    while C3.is_pressed:
      if C3.is_pressed == False:
        break